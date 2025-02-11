# -*- coding: utf-8 -*-

from odoo import fields, models  # type: ignore

# Modelo Usuario
class Usuario(models.Model):
    _name = 'vilaexplorer.usuario'
    _description = 'Modelo para la entidad Usuario'
    _rec_name = "nombre"
    _inherit = 'image.mixin'

    id_usuario = fields.Integer(
        string='ID Usuario', required=True, readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('vilaexplorer.usuario')
    )
    
    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    password = fields.Char(string='Contraseña', required=True)
    activo = fields.Boolean(string='Activo', default=True)
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today)

    # Relación con roles históricos (One-to-Many)
    roles = fields.One2many(
        comodel_name='vilaexplorer.usuario_rol', 
        inverse_name='usuario_id', 
        string='Roles Históricos'
    )

    # Rol actual del usuario (Many-to-One)
    rol_actual_id = fields.Many2one(
        comodel_name='vilaexplorer.rol', 
        string='Rol Actual'
    )
    
    articulos = fields.One2many(
        comodel_name="vilaexplorer.articulo",
        inverse_name="autor_id",
        string="Mis articulos"
    )
    
    favoritos = fields.One2many(
        comodel_name="vilaexplorer.favorito",
        inverse_name="usuario_id"
    )
    
    fiesta_tradicion = fields.One2many(
        comodel_name="vilaexplorer.fiesta_tradicion",
        inverse_name="autor_id"
    )
    
    mis_platos = fields.One2many(
        comodel_name="vilaexplorer.plato",
        inverse_name="autor_id",
        string="Mis platos"
    )
    
    mis_platos_aprobados = fields.One2many(
        comodel_name="vilaexplorer.plato",
        inverse_name="aprobador_id",
        string="Mis platos aprobados" 
    )
    
    puntuaciones = fields.One2many(
        comodel_name="vilaexplorer.puntuacion",
        inverse_name="usuario_id",
        string="Mis puntuaciones" 
    )
    
    mis_rutas = fields.One2many(
        comodel_name="vilaexplorer.ruta",
        inverse_name="autor_id",
        string="Mis platos aprobados" 
    )