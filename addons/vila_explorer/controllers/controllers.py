# -*- coding: utf-8 -*-
# from odoo import http


# class VilaExplorer(http.Controller):
#     @http.route('/vila_explorer/vila_explorer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vila_explorer/vila_explorer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vila_explorer.listing', {
#             'root': '/vila_explorer/vila_explorer',
#             'objects': http.request.env['vila_explorer.vila_explorer'].search([]),
#         })

#     @http.route('/vila_explorer/vila_explorer/objects/<model("vila_explorer.vila_explorer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vila_explorer.object', {
#             'object': obj
#         })
