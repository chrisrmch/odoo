# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api # type: ignore

_logger = logging.getLogger(__name__)

# Modelo Rol
class Rol(models.Model):
    _name = 'vilaexplorer.rol'
    _description = 'Entidad que representa un rol en el sistema'
    _rec_name='nombre'
    
    codigo = fields.Char(string='Código del Rol', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.rol'))
    nombre = fields.Char(string='Nombre del Rol', required=True)
    group_id = fields.Many2one('res.groups', string='Grupo Asociado', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    
    usuarios = fields.One2many(
        comodel_name="vilaexplorer.usuario",
        inverse_name="rol_actual_id",
        string="Usuarios que pertenecen a este rol" 
    )
    
    usuario_rol = fields.One2many(
        comodel_name="vilaexplorer.usuario_rol",
        inverse_name="rol_id", 
    )
    
    