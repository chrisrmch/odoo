# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo CategoriaPlato
class CategoriaPlato(models.Model):
    _name = 'vilaexplorer.categoria_plato'
    _description = 'Entidad que representa una categoría de plato de la carta de un restaurante'
    _rec_name = 'nombre_categoria'
    
    id_categoria_plato = fields.Integer(string='ID Categoría', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.categoria_plato'))
    nombre_categoria = fields.Char(string='Nombre de la Categoría', required=True)
    activo = fields.Boolean(string='Activo', default=True)
