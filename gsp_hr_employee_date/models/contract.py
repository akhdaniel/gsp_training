from odoo import models, fields, api

class contract(models.Model):
    _inherit = "hr.contract"

    tanggal_aktif = fields.Date(string="Tanggal aktif")
    employee_id = fields.Many2one(string="Karyawan", comodel_name="hr.employee" )
    