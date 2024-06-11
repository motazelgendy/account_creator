# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account__creator_esnad(models.Model):
    _inherit = 'res.partner'


    @api.model
    def create(self, vals):
     account_receivable_ids =  self.env['account.account'].search([('account_type','=','asset_receivable')])


     accoutcodes = []
     for id in account_receivable_ids:
         accoutcodes.append(id.code)


     account_codes = [eval(i) for i in accoutcodes]
     account_code = min(account_codes) - 1

     account_receivable_data = {
         'code' : str(account_code),
         'name' : vals['name'],
         'account_type' : 'asset_receivable'

     }


     account_receivable_id = self.env['account.account'].create(account_receivable_data)
     vals['property_account_receivable_id'] = account_receivable_id
     return super().create(vals)



