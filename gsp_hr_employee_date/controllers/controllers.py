# -*- coding: utf-8 -*-
from odoo import http

# class GspHrEmployeeDate(http.Controller):
#     @http.route('/gsp_hr_employee_date/gsp_hr_employee_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gsp_hr_employee_date/gsp_hr_employee_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gsp_hr_employee_date.listing', {
#             'root': '/gsp_hr_employee_date/gsp_hr_employee_date',
#             'objects': http.request.env['gsp_hr_employee_date.gsp_hr_employee_date'].search([]),
#         })

#     @http.route('/gsp_hr_employee_date/gsp_hr_employee_date/objects/<model("gsp_hr_employee_date.gsp_hr_employee_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gsp_hr_employee_date.object', {
#             'object': obj
#         })