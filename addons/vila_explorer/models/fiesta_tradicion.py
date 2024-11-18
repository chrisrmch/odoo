# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FiestaTradicion(models.Model):
    _name = 'vilaexplorer.fiesta_tradicion'
    _description = 'Entidad que representa una fiesta o tradición de la región'
    _rec_name = 'nombre'
    _inherit = ['image.mixin']  # Heredar de image.mixin para usar las capacidades de imagen integradas
    
    id_fiesta_tradicion = fields.Integer(string='ID Fiesta Tradición', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.fiesta_tradicion'))
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    autor_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Autor', required=True)
    
    # Este campo ya se gestiona mediante el mixin
    # El campo `image_1920` ahora se usará para almacenar la imagen principal
