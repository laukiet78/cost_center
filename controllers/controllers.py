# -*- coding: utf-8 -*-
from odoo import http

# class Addons-reports/costCenter(http.Controller):
#     @http.route('/addons-reports/cost_center/addons-reports/cost_center/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons-reports/cost_center/addons-reports/cost_center/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons-reports/cost_center.listing', {
#             'root': '/addons-reports/cost_center/addons-reports/cost_center',
#             'objects': http.request.env['addons-reports/cost_center.addons-reports/cost_center'].search([]),
#         })

#     @http.route('/addons-reports/cost_center/addons-reports/cost_center/objects/<model("addons-reports/cost_center.addons-reports/cost_center"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons-reports/cost_center.object', {
#             'object': obj
#         })