# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore

# Modelo Coordenadas
class Coordenadas(models.Model):
    _name = 'vilaexplorer.coordenadas'
    _description = 'Entidad que representa las coordenadas de un lugar de interés o de una ruta'
    _rec_name='id_coordenadas'
    
    id_coordenadas = fields.Integer(string='ID Coordenadas', required=True, readonly=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.coordenadas'))
    latitud = fields.Float(string='Latitud', required=True)
    longitud = fields.Float(string='Longitud', required=True)
    lugar_interes_id = fields.Many2one(comodel_name='vilaexplorer.lugar_interes', string='Lugar de Interés')
    ruta_id = fields.Many2one(comodel_name='vilaexplorer.ruta', string='Ruta')