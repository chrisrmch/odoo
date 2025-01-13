# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore

# Modelo Puntuacion
class Puntuacion(models.Model):
    _name = 'vilaexplorer.puntuacion'
    _description = 'Entidad que representa una puntuación'
    _rec_name = 'id_puntuacion'

    id_puntuacion = fields.Integer(
        string='ID Puntuación', 
        required=True, 
        index=True, 
        default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.puntuacion')
    )
    puntuacion = fields.Integer(
        string='Puntuación', 
        required=True
    )
    usuario_id = fields.Many2one(
        comodel_name='vilaexplorer.usuario', 
        string='Usuario', 
        required=True
    )
    id_entidad = fields.Integer(
        string='ID Entidad', 
        required=True
    )
    tipo_entidad = fields.Selection(
        [
            ('PLATO', 'Plato'), 
            ('LUGAR_INTERES', 'Lugar de Interés'), 
            ('FIESTA_TRADICION', 'Fiesta Tradición'), 
            ('ARTICULO', 'Artículo')
        ], 
        string='Tipo de Entidad', 
        required=True
    )

    promedio_puntuacion = fields.Float(
        string='Promedio de Puntuación', 
        compute='_compute_promedio_puntuacion', 
        store=True,
        help='Promedio de todas las puntuaciones registradas para la misma entidad.'
    )

    _sql_constraints = [
        ('puntuacion_range', 'CHECK(puntuacion >= 1 AND puntuacion <= 5)', 'La puntuación debe estar entre 1 y 5.')
    ]

    @api.depends('id_entidad', 'tipo_entidad')
    def _compute_promedio_puntuacion(self):
        for record in self:
            puntuaciones = self.search([
                ('id_entidad', '=', record.id_entidad),
                ('tipo_entidad', '=', record.tipo_entidad)
            ])
            if puntuaciones:
                record.promedio_puntuacion = sum(p.puntuacion for p in puntuaciones) / len(puntuaciones)
            else:
                record.promedio_puntuacion = 0.0
