# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo UsuarioRol
class UsuarioRol(models.Model):
    _name = 'vilaexplorer.usuario_rol'
    _description = 'Entidad que representa la asignación de un rol a un usuario'

    usuario_id = fields.Many2one(
        'vilaexplorer.usuario',
        string='Usuario',
        required=True,
        ondelete='cascade'  # Elimina los registros relacionados automáticamente
    )
    rol_id = fields.Many2one('vilaexplorer.rol', string='Rol', required=True)
    fecha_de_asignacion = fields.Date(string='Fecha de Asignación', default=fields.Date.today)