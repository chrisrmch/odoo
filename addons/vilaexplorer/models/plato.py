# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions  # type: ignore

# Modelo Plato
class Plato(models.Model):
    _name = 'vilaexplorer.plato'
    _description = 'Entidad que representa un plato en la base de datos'
    _rec_name = 'nombre'
    _inherit = ['image.mixin']  # Heredar de image.mixin para usar las capacidades de imagen integradas

    id_plato = fields.Integer(string='ID Plato', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.plato'))
    nombre = fields.Char(string='Nombre del Plato', required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    ingredientes = fields.Text(string='Ingredientes', required=True)
    receta = fields.Text(string='Receta', required=True)
    estado = fields.Boolean(string='Estado de Aprobación', default=False)
    tipo_plato_id = fields.Many2one(comodel_name='vilaexplorer.tipo_plato', string='Tipo de Plato', required=True)
    autor_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Autor', required=True)
    aprobador_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Aprobador')

    # Los campos de imagen ya vienen definidos por image.mixin (como image_1920, image_128, etc.)