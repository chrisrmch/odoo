# -*- coding: utf-8 -*-

from odoo import models, fields

# Modelo Usuario
class Usuario(models.Model):
    _name = 'vilaexplorer.usuario'
    _description = 'Modelo para la entidad Usuario'
    _rec_name = 'nombre'

    id_usuario = fields.Integer(
        string='ID Usuario', required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.usuario')
    )
    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    password = fields.Char(string='Contraseña', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)

    # Relación con roles históricos (One-to-Many)
    roles = fields.One2many(
        comodel_name='vilaexplorer.usuario_rol', 
        inverse_name='usuario_id', 
        string='Roles Históricos'
    )

    # Rol actual del usuario (Many-to-One)
    rol_actual_id = fields.Many2one(
        comodel_name='vilaexplorer.rol', 
        string='Rol Actual'
    )
