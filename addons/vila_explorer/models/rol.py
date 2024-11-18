# -*- coding: utf-8 -*-

from odoo import models, fields


# Modelo Rol
class Rol(models.Model):
    _name = 'vilaexplorer.rol'
    _description = 'Entidad que representa un rol en el sistema'
    _rec_name = 'nombre'
    
    id = fields.Integer(string='ID', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.rol'))
    nombre = fields.Char(string='Nombre del Rol', required=True)
    activo = fields.Boolean(string='Activo', default=True)
