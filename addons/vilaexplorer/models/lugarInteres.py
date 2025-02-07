# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo LugarInteres
class LugarInteres(models.Model):
    _name = 'vilaexplorer.lugar_interes'
    _description = 'Entidad que representa un lugar de interés turístico'
    _rec_name='nombre_lugar'
    
    id_lugar_interes = fields.Integer(string='ID Lugar de Interés', readonly=True,  required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.lugar_interes'))
    nombre_lugar = fields.Char(string='Nombre del Lugar', required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    fecha_alta = fields.Date(string='Fecha de Alta', required=True, default=fields.Date.today)
    imagen = fields.Char(string='URL de la Imagen', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    tipo_lugar_id = fields.Many2one(comodel_name='vilaexplorer.tipo_lugar_interes', string='Tipo de Lugar', required=True)
    coordenadas_ids = fields.One2many(comodel_name='vilaexplorer.coordenadas', inverse_name='lugar_interes_id', string='Coordenadas Asociadas')