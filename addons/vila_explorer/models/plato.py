# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions  # type: ignore

# Modelo Plato
class Plato(models.Model):
    _name = 'vilaexplorer.plato'
    _description = 'Entidad que representa un plato en la base de datos'
    _rec_name = 'nombre'
    _inherit = ['image.mixin']  # Heredar de image.mixin para usar las capacidades de imagen integradas

    id_plato = fields.Integer(
        string='ID Plato', 
        required=True, 
        index=True, 
        default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.plato'),
        readonly=True,
        help='Identificador único del plato.'
    )
    nombre = fields.Char(
        string='Nombre del Plato', 
        required=True,
        help='Nombre descriptivo del plato.',
        placeholder='Introduce el nombre del plato...',
        max_width=150
    )
    descripcion = fields.Text(
        string='Descripción', 
        required=True,
        help='Descripción breve del plato.',
        placeholder='Escribe una descripción...',
        max_height=500
    )
    ingredientes = fields.Text(
        string='Ingredientes', 
        required=True,
        help='Lista de ingredientes del plato.',
        placeholder='Escribe los ingredientes aquí...',
        max_height=300
    )
    receta = fields.Text(
        string='Receta', 
        required=True,
        help='Instrucciones para preparar el plato.',
        placeholder='Escribe la receta aquí...',
        max_height=1000
    )
    estado = fields.Boolean(
        string='Estado de Aprobación', 
        default=False,
        help='Indica si el plato ha sido aprobado.'
    )
    tipo_plato_id = fields.Many2one(
        comodel_name='vilaexplorer.tipo_plato', 
        string='Tipo de Plato', 
        required=True,
        help='Tipo al que pertenece el plato.'
    )
    autor_id = fields.Many2one(
        comodel_name='vilaexplorer.usuario', 
        string='Autor', 
        required=True,
        help='Usuario que creó el plato.'
    )
    aprobador_id = fields.Many2one(
        comodel_name='vilaexplorer.usuario', 
        string='Aprobador',
        help='Usuario que aprobó el plato.'
    )
    puntuacion = fields.One2many(
        comodel_name = 'vilaexplorer.puntuacion',
        string='Aprobador'
    )

    @api.constrains('nombre')
    def _check_nombre_length(self):
        for record in self:
            if len(record.nombre) > 150:
                raise exceptions.ValidationError("El nombre del plato no puede superar los 150 caracteres.")
