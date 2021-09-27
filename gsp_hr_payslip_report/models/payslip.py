# -*- coding: utf-8 -*-

from odoo import models, fields, api

class payslip(models.Model):
    _inherit = 'hr.payslip'

    basic = fields.Float(string="Basic", compute="_get_nett")
    nett = fields.Float(string="Nett", compute="_get_nett")
    tunj = fields.Float(string="Tunjangan", compute="_get_nett")
    pot = fields.Float(string="Potogan", compute="_get_nett")



    def _get_nett(self):
        for rec in self:
            nett = 0
            basic = 0
            gross = 0
            tunj = 0
            pot = 0
            
            for line in rec.line_ids:
                if line.code == 'BASIC':
                    basic = line.total
                if line.code == 'GROSS':
                    gross = line.total
                if line.code == 'NET':
                    nett = line.total

            rec.tunj = gross - basic
            rec.pot = nett - gross
            rec.nett = nett
            rec.basic = basic
