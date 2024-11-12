# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


class gastronomia(models.Model):
    _name = 'vila_explorer.gastronomia'
    
    id = fields.Integer(required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilae_explorer.gastronomia'))
    nombre = fields.Char()
    descripcion = fields.Char()
    ingredientes = fields.Text()
    receta = fields.Text()
    estado = fields.Boolean()
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user, readonly=True)
