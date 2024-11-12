# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore

class fiesta_tradicion(models.Model):
    _name = 'vila_explorer.fiesta_tradicion'

    id = fields.Integer(required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilae_explorer.fiesta_tradicion'))
    nombre = fields.Char(string='Nombre')
    descripcion = fields.Char(string="descripcion")
    imagen = fields.Binary(string="imagen")
    
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, readonly=True)