# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

# Modelo Usuario
class Usuario(models.Model):
    _name = 'vilaexplorer.usuario'
    _description = 'Modelo para la entidad Usuario'
    _rec_name = 'nombre'
    
    id_usuario = fields.Integer(string='ID Usuario', required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.usuario'))
    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    password = fields.Char(string='Contraseña', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)
    roles = fields.One2many(comodel_name='vilaexplorer.usuario_rol', inverse_name='usuario_id', string='Roles Históricos')
    rol_actual_id = fields.Many2one(comodel_name='vilaexplorer.rol', string='Rol Actual')
    
    @api.model
    def create(self, vals):
        # Crear el registro del usuario
        usuario = super(Usuario, self).create(vals)
        # Agregar el rol actual al histórico de roles si existe
        if 'rol_actual_id' in vals and vals['rol_actual_id']:
            self.env['vilaexplorer.usuario_rol'].create({
                'usuario_id': usuario.id,
                'rol_id': vals['rol_actual_id'],
                'fecha_de_asignacion': fields.Date.today(),
            })
        return usuario

    def write(self, vals):
        # Llamar al método super para realizar la actualización del usuario
        res = super(Usuario, self).write(vals)
        for usuario in self:
            # Si se está cambiando el rol actual, agregarlo al histórico de roles
            if 'rol_actual_id' in vals and vals['rol_actual_id']:
                self.env['vilaexplorer.usuario_rol'].create({
                    'usuario_id': usuario.id,
                    'rol_id': vals['rol_actual_id'],
                    'fecha_de_asignacion': fields.Date.today(),
                })
        return res