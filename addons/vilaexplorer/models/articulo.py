# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions # type: ignore


# Modelo Articulo
class Articulo(models.Model):
    _name = 'vilaexplorer.articulo'
    _description = 'Entidad que representa un artículo escrito por un redactor'
    _rec_name = "titulo"

    id = fields.Integer(
        string='ID', 
        required=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.articulo'),
        readonly=True,
        help='Identificador único del artículo.'
    )
    contenido = fields.Text(
        string='Contenido', 
        required=True,
        help='Texto completo del artículo.',
    )
    fecha_publicacion = fields.Date(
        string='Fecha de Publicación', 
        help='Fecha en la que se publicó el artículo.',
        readonly=True
    )
    titulo = fields.Char(
        string='Título', 
        required=True,
        help='Título descriptivo del artículo.',
        max_width=200
    )
    autor_id = fields.Many2one(
        comodel_name='vilaexplorer.usuario', 
        string='Autor',
        required=True,
        help='Usuario que redactó el artículo.'
    )

    @api.constrains('titulo')
    def _check_titulo_length(self):
        for record in self:
            if len(record.titulo) > 200:
                raise exceptions.ValidationError("El título no puede superar los 200 caracteres.")