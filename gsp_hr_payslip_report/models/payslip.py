# -*- coding: utf-8 -*-

from odoo import models, fields, api

class payslip(models.Model):
    _inherit = 'hr.payslip'

    nett = fields.Float(string="Nett", compute="_get_nett")



    def _get_nett(self):
        for rec in self:
            nett = 0
            for line in rec.line_ids:
                if line.code == 'NET':
                    nett = line.total
            rec.nett = nett
