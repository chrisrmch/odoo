# -*- coding: utf-8 -*-
# from odoo import http


# class VilaExplorer(http.Controller):
#     @http.route('/vilaexplorer/vilaexplorer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vilaexplorer/vilaexplorer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vilaexplorer.listing', {
#             'root': '/vilaexplorer/vilaexplorer',
#             'objects': http.request.env['vilaexplorer.vilaexplorer'].search([]),
#         })

#     @http.route('/vilaexplorer/vilaexplorer/objects/<model("vilaexplorer.vilaexplorer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vilaexplorer.object', {
#             'object': obj
#         })
