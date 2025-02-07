# -*- coding: utf-8 -*-

from odoo import models, fields # type: ignore


# Modelo Favorito
class Favorito(models.Model):
    _name = 'vilaexplorer.favorito'
    _description = 'Entidad que representa la relación entre un usuario y una entidad marcada como favorita'
    _rec_name='id_favorito'
    
    id_favorito = fields.Integer(string='ID Favorito', required=True, index=True, default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.favorito'))
    usuario_id = fields.Many2one(comodel_name='vilaexplorer.usuario', string='Usuario', required=True)
    id_entidad = fields.Integer(string='ID Entidad', required=True)
    tipo_entidad = fields.Selection([('PLATO', 'Plato'), ('ARTICULO', 'Artículo'), ('RUTA', 'Ruta'), ('LUGAR_INTERES', 'Lugar de Interés')], string='Tipo de Entidad', required=True)