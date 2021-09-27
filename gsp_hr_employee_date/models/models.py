# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class gsp_hr_employee_date(models.Model):
#     _name = 'gsp_hr_employee_date.gsp_hr_employee_date'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100