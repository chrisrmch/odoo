# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore

# Modelo TipoPlato
class TipoPlato(models.Model):
    _name = 'vilaexplorer.tipo_plato'
    _description = 'Tipo de plato'
    _rec_name='nombre_tipo'
    
    id_tipo_plato = fields.Integer(string='ID Tipo Plato', readolny=True, required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.tipo_plato'))
    nombre_tipo = fields.Char(string='Nombre del Tipo de Plato', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    categoria_plato_id = fields.Many2one(comodel_name='vilaexplorer.categoria_plato', string='Categoría del Plato', required=True)
    platos = fields.One2many(comodel_name="vilaexplorer.plato", inverse_name="tipo_plato_id")
    