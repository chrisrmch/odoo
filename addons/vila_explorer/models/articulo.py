# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo Articulo
class Articulo(models.Model):
    _name = 'vilaexplorer.articulo'
    _description = 'Entidad que representa un artículo escrito por un redactor'
    _rec_name = 'titulo'
    
    id = fields.Integer(string='ID', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.articulo'))
    contenido = fields.Text(string='Contenido', required=True)
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    titulo = fields.Char(string='Título', required=True)
    autor_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Autor', required=True)
