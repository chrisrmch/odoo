# -*- coding: utf-8 -*-

from odoo import models, fields


class usuarios(models.Model):
    _name = 'vila_explorer.usuarios'
    
    id_usuario = fields.Integer(required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilae_explorer.gastronomia'))
    nombre = fields.Char()
    email = fields.Char()
    password = fields.Char()
    fecha_creacion = fields.Date(default=fields.Date.today)