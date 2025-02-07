# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore

# Modelo UsuarioRol
class UsuarioRol(models.Model):
    _name = 'vilaexplorer.usuario_rol'
    _description = 'Entidad que representa la asignación de un rol a un usuario'
    _rec_name='id'

    id = fields.Integer(string='ID', required=True, index=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.usuario_rol'))
    usuario_id = fields.Many2one(
        comodel_name='vilaexplorer.usuario',
        string='Usuario',
        required=True,
        ondelete='cascade'
    )
    rol_id = fields.Many2one(comodel_name='vilaexplorer.rol', string='Rol', required=True)
    fecha_de_asignacion = fields.Date(string='Fecha de Asignación', default=fields.Date.today)