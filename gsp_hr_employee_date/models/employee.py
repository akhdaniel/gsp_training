from odoo import models, fields, api

class employee(models.Model):
    _inherit = "hr.employee"

    tanggal_masuk = fields.Date(string="Tanggal masuk")
    