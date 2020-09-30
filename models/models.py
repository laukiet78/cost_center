# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CenterCost(models.Model):
    _inherit = 'account.analytic.line'

    analytic_mather = fields.Many2one('account.analytic.account', 'Cuenta madre', store=True, related="account_id.parent_id")

    debit = fields.Monetary(string="Debe", store=True, related="move_id.debit")
    credit = fields.Monetary(string="Haber", store=True, related="move_id.credit")