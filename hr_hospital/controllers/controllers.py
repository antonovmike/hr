# -*- coding: utf-8 -*-
# from odoo import http


# class Antonovmike/hr/hrHospital(http.Controller):
#     @http.route('/antonovmike/hr/hr_hospital/antonovmike/hr/hr_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/antonovmike/hr/hr_hospital/antonovmike/hr/hr_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('antonovmike/hr/hr_hospital.listing', {
#             'root': '/antonovmike/hr/hr_hospital/antonovmike/hr/hr_hospital',
#             'objects': http.request.env['antonovmike/hr/hr_hospital.antonovmike/hr/hr_hospital'].search([]),
#         })

#     @http.route('/antonovmike/hr/hr_hospital/antonovmike/hr/hr_hospital/objects/<model("antonovmike/hr/hr_hospital.antonovmike/hr/hr_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('antonovmike/hr/hr_hospital.object', {
#             'object': obj
#         })
