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
        
        # Asegurar que solo un rol de Vila Explorer sea seleccionado
        if 'groups_id' in vals:
            vals['groups_id'] = self._filter_vila_explorer_groups(vals['groups_id'])

        user = super(ResUsers, self).create(vals)
        _logger.info(f"Usuario creado en res.users: {user.id} ({user.login})")

        try:
            # Procesar grupos y buscar rol actual
            group_ids = [group[1] for group in vals.get('groups_id', []) if group[0] == 4]
            _logger.info(f"Procesando grupos: {group_ids}")
            rol_actual = self.env['vilaexplorer.rol'].search([('group_id', 'in', group_ids)], limit=1)
            _logger.info(f"Rol encontrado: {rol_actual.name if rol_actual else 'Ninguno'}")

            # Crear el usuario en vilaexplorer.usuario
            usuario = self.env['vilaexplorer.usuario'].create({
                'id_usuario': user.id,
                'nombre': vals.get('name', user.name),
                'email': vals.get('login', user.login),
                'password': vals.get('password', ''),
                'activo': True,
                'rol_actual_id': rol_actual.id if rol_actual else None,
                'fecha_creacion': fields.Date.today(),
            })
            _logger.info(f"Usuario creado en vilaexplorer.usuario con ID: {usuario.id_usuario}")
        except Exception as e:
            _logger.error(f"Error creando el usuario en vilaexplorer.usuario: {e}")

        return user

    def write(self, vals):
        """
        Sobreescribir el método write para actualizar un usuario en vilaexplorer.usuario al modificar un usuario del sistema
        """
        if 'groups_id' in vals:
            vals['groups_id'] = self._filter_vila_explorer_groups(vals['groups_id'])

        res = super(ResUsers, self).write(vals)

        for user in self:
            try:
                # Buscar el usuario en vilaexplorer.usuario
                usuario_vilaexplorer = self.env['vilaexplorer.usuario'].search([('email', '=', user.login)], limit=1)
                if usuario_vilaexplorer:
                    group_ids = [group[1] for group in vals.get('groups_id', []) if group[0] == 4]
                    rol_actual = self.env['vilaexplorer.rol'].search([('group_id', 'in', group_ids)], limit=1)

                    usuario_vilaexplorer.write({
                        'nombre': vals.get('name', user.name),
                        'email': vals.get('login', user.login),
                        'password': vals.get('password', usuario_vilaexplorer.password),
                        'rol_actual_id': rol_actual.id if rol_actual else usuario_vilaexplorer.rol_actual_id.id,
                    })
                    _logger.info(f"Usuario actualizado en vilaexplorer.usuario: {usuario_vilaexplorer.id_usuario}")
            except Exception as e:
                _logger.error(f"Error actualizando el usuario en vilaexplorer.usuario: {str(e)}")

        return res

    def unlink(self):
        """
        Sobreescribir el método unlink para eliminar el usuario correspondiente en vilaexplorer.usuario
        cuando se elimine un usuario en res.users
        """
        for user in self:
            try:
                # Buscar y eliminar el usuario correspondiente en vilaexplorer.usuario
                usuario_vilaexplorer = self.env['vilaexplorer.usuario'].search([('email', '=', user.login)], limit=1)
                if usuario_vilaexplorer:
                    usuario_vilaexplorer.unlink()
                    _logger.info(f"Usuario eliminado en vilaexplorer.usuario: {usuario_vilaexplorer.id_usuario}")
            except Exception as e:
                _logger.error(f"Error eliminando el usuario en vilaexplorer.usuario: {str(e)}")
        
        # Eliminar el usuario en res.users
        return super(ResUsers, self).unlink()

    def _filter_vila_explorer_groups(self, groups):
        """
        Filtra los grupos para asegurar que solo se seleccione un grupo de Vila Explorer.
        """
        vila_explorer_group_ids = [
            self.env.ref('vilaexplorer.group_vilaexplorer_usuario').id,
            self.env.ref('vilaexplorer.group_vilaexplorer_administrador').id,
            self.env.ref('vilaexplorer.group_vilaexplorer_redactor').id,
        ]

        # Obtener los IDs de los grupos de Vila Explorer seleccionados
        selected_vila_groups = [group_id for operation, group_id in groups if operation == 4 and group_id in vila_explorer_group_ids]

        if selected_vila_groups:
            # Filtrar y mantener solo el último grupo seleccionado
            groups = [(op, gid) for op, gid in groups if gid not in vila_explorer_group_ids] + [(4, selected_vila_groups[-1])]
        
        return groups
