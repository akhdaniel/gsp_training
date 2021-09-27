from odoo import models, fields, api

class contract(models.Model):
    _inherit = "hr.contract"

    tanggal_aktif = fields.Date(string="Tanggal aktif")
    