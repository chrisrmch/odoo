# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

# Modelo ResUsers para sincronizar con Usuario
class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        _logger.info(f"Creando usuario en res.users con datos: {vals}")
        
        # self == res.users
        # ResUsers es la instancia de la propia clase 
        # odoo.addons.vila_explorer.models.resUser.ResUsers
        # vals son todos los valores con los que se crea el usuario en res.users
        user = super(ResUsers, self).create(vals)
        try:
            # Buscar la categoría "Vila Explorer"
            # self.env es un método que permite acceder a cualquier tabla del entorno de Odoo
            category = self.env['ir.module.category'].search([('name', '=', 'Vila Explorer')], limit=1)
            if not category:
                _logger.warning("No se encontró la categoría 'Vila Explorer'.")
                return user
            
            # Obtener los grupos del usuario dentro de "Vila Explorer"
            # Obtiene el user de res.users y busca el atributo groups_id que contiene una lista de grupos
            # hace un filtrado de estos grupos por el id de la categoria. 
            vila_groups = user.groups_id.filtered(lambda g: g.category_id == category)
            _logger.info(f"Grupos asociados al usuario: {[group.name for group in vila_groups]}")
            
            # Buscar el rol correspondiente
            rol_actual = self.env['vilaexplorer.rol'].search([('group_id', 'in', vila_groups.ids)], limit=1)

            # Crear el usuario en vilaexplorer.usuario si no existe ya
            existing_usuario = self.env['vilaexplorer.usuario'].search([('email', '=', user.login)], limit=1)
            if not existing_usuario:
                self.env['vilaexplorer.usuario'].create(
                    {
                    'id_usuario': user.id,
                    'nombre': vals.get('name', user.name),
                    'email': vals.get('login', user.login),
                    'password': vals.get('password', ''),
                    'activo': True,
                    'rol_actual_id': rol_actual.id if rol_actual else None,
                    'fecha_creacion': fields.Date.today(),
                }
                    )
                _logger.info(f"Usuario creado en vilaexplorer.usuario: {user.id}")
            else:
                _logger.warning("El usuario ya existe en vilaexplorer.usuario.")

        except Exception as e:
            _logger.error(f"Error al crear el usuario en vilaexplorer.usuario: {str(e)}")

        return user

    def write(self, vals):
        """
        Sobreescribir el método write para actualizar roles históricos cuando cambian los grupos
        """
        _logger.info(f"vals: {vals}")

        vila_explorer_group_ids = [
            self.env.ref('vila_explorer.group_vilaexplorer_client').id,
            self.env.ref('vila_explorer.group_vilaexplorer_admin').id,
            self.env.ref('vila_explorer.group_vilaexplorer_editor').id,
        ]

        # Procesar grupos seleccionados
        group_keys = [key for key in vals if key.startswith('in_group_')]
        if group_keys:
            groups_to_remove = [(3, gid) for gid in vila_explorer_group_ids]  # Eliminar todos los grupos
            groups_to_add = [(4, int(key.split('_')[-1])) for key in group_keys if vals[key]]  # Añadir seleccionados
            vals['groups_id'] = groups_to_remove + groups_to_add
            _logger.info(f"Grupos actualizados en groups_id: {vals['groups_id']}")

        # Filtrar grupos para mantener solo el último grupo seleccionado
        if 'groups_id' in vals:
            vals['groups_id'] = self._filter_vila_explorer_groups(vals['groups_id'])
            _logger.info(f"Grupos después de filtrar: {vals['groups_id']}")

        # Actualizar usuario en el modelo base
        res = super(ResUsers, self).write(vals)

        # Actualizar vilaexplorer.usuario
        for user in self:
            try:
                usuario_vilaexplorer = self.env['vilaexplorer.usuario'].search([('email', '=', user.login)], limit=1)
                if usuario_vilaexplorer:
                    # Obtener los IDs de los grupos seleccionados
                    group_ids = [group[1] for group in vals.get('groups_id', []) if group[0] == 4]

                    # Buscar el nuevo rol asociado al grupo
                    nuevo_rol = self.env['vilaexplorer.rol'].search([('group_id', 'in', group_ids)], limit=1)

                    # Si el rol cambia, registrar en roles históricos
                    if usuario_vilaexplorer.rol_actual_id != nuevo_rol:
                        self.env['vilaexplorer.usuario_rol'].create({
                            'usuario_id': usuario_vilaexplorer.id,
                            'rol_id': usuario_vilaexplorer.rol_actual_id.id,  # Rol anterior
                            'fecha_de_asignacion': fields.Date.today(),
                        })
                        _logger.info(f"Registrado rol histórico para usuario {usuario_vilaexplorer.nombre}: {usuario_vilaexplorer.rol_actual_id.nombre}")

                    # Actualizar el rol actual
                    usuario_vilaexplorer.write({
                        'rol_actual_id': nuevo_rol.id if nuevo_rol else usuario_vilaexplorer.rol_actual_id.id,
                    })

            except Exception as e:
                _logger.error(f"Error actualizando el usuario en vilaexplorer.usuario: {str(e)}")

        return res



    def unlink(self):
        """
        Sobreescribir el método unlink para permitir la eliminación de usuarios inactivos y
        asegurarse de que también se eliminen de vilaexplorer.usuario.
        """
        # Filtrar usuarios inactivos y activos
        inactive_users = self.filtered(lambda u: not u.active)
        active_users = self - inactive_users

        # Eliminar usuarios de vilaexplorer.usuario
        for user in self:
            try:
                usuario_vilaexplorer = self.env['vilaexplorer.usuario'].search([('email', '=', user.login)], limit=1)
                if usuario_vilaexplorer:
                    _logger.info(f"Eliminando usuario en vilaexplorer.usuario: {usuario_vilaexplorer.id_usuario}")
                    usuario_vilaexplorer.unlink()
            except Exception as e:
                _logger.error(f"Error eliminando usuario en vilaexplorer.usuario para {user.login}: {str(e)}")

        # Eliminar usuarios inactivos sin revisar la plantilla de portal
        if inactive_users:
            _logger.info(f"Eliminando usuarios inactivos: {[u.login for u in inactive_users]}")
            super(ResUsers, inactive_users).unlink()

        # Proceder con la eliminación normal para usuarios activos
        if active_users:
            _logger.info(f"Eliminando usuarios activos: {[u.login for u in active_users]}")
            return super(ResUsers, active_users).unlink()

        return True



    def _filter_vila_explorer_groups(self, groups):
        """
        Mantiene solo el último grupo de Vila Explorer seleccionado.
        """
        vila_explorer_group_ids = [
            self.env.ref('vila_explorer.group_vilaexplorer_client').id,
            self.env.ref('vila_explorer.group_vilaexplorer_admin').id,
            self.env.ref('vila_explorer.group_vilaexplorer_editor').id,
        ]

        # Obtener el último grupo seleccionado
        selected_vila_groups = [group_id for op, group_id in groups if op == 4 and group_id in vila_explorer_group_ids]

        # Eliminar todos los grupos de Vila Explorer y añadir solo el último seleccionado
        if selected_vila_groups:
            return [(3, gid) for gid in vila_explorer_group_ids] + [(4, selected_vila_groups[-1])]
        return groups