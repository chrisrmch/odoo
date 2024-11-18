# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo Ruta
class Ruta(models.Model):
    _name = 'vilaexplorer.ruta'
    _description = 'Entidad que representa una ruta turística'
    _rec_name = 'nombre_ruta'
    
    id_ruta = fields.Integer(string='ID Ruta', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.ruta'))
    nombre_ruta = fields.Char(string='Nombre de la Ruta', required=True)
    autor_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Autor', required=True)
    coordenadas_ids = fields.One2many(comodel_name='vilaexplorer.coordenadas', inverse_name='ruta_id', string='Coordenadas de la Ruta')