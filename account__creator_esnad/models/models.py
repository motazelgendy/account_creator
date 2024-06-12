# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account__creator_esnad(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        account_receivable_ids = self.env['account.account'].search([('account_type', '=', 'asset_receivable')])

        accoutcodes = []
        for id in account_receivable_ids:
            accoutcodes.append(id.code)

        account_codes = [eval(i) for i in accoutcodes]
        account_code = min(account_codes) - 1

        account_receivable_data = {
            'code': str(account_code),
            'name': vals['name'],
            'account_type': 'asset_receivable'

        }

        account_receivable_id = self.env['account.account'].create(account_receivable_data)
        vals['property_account_receivable_id'] = account_receivable_id
        partner_id = super().create(vals)
        analytical_account_ids = self.env['account.analytic.plan'].search([('name', '=', 'Projects')])

        analytical_accounts = []
        for analytic_acc in analytical_account_ids:
            analytical_accounts.append(analytic_acc.id)
        analytical_account_data = {
            'name': vals['name'],
            'plan_id': analytical_accounts[0],
            'partner_id' : int(partner_id)



        }
        analytical_account_id = self.env['account.analytic.account'].create(analytical_account_data)

        return partner_id

