# -*- coding: utf-8 -*-

from odoo import models, fields


# Modelo TipoLugarInteres
class TipoLugarInteres(models.Model):
    _name = 'vilaexplorer.tipo_lugar_interes'
    _description = 'Entidad que representa un tipo de lugar de interés turístico'
    _rec_name = 'nombre_tipo'
    
    id_tipo_lugar = fields.Integer(string='ID Tipo Lugar', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.tipo_lugar_interes'))
    nombre_tipo = fields.Char(string='Nombre del Tipo de Lugar', required=True)
