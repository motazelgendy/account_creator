# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account__creator_esnad(models.Model):
    _inherit = 'res.partner'


    @api.model
    def create(self, vals):
     account_receivable_ids =  self.env['account.account'].search([('account_type','=','Receivable')])
     ccount_receivable_code =  self.env['account.account'].browse(account_receivable_ids).mapped('code')
     accoutcodes = []
     for id in ccount_receivable_code:
         accoutcodes.append(int(id))


     account_code = max(accoutcodes)

     account_name = vals['name']
     account_receivable_id = self.env['account.account'].create({'code':account_code,'name':account_code,'account_type':'asset_receivable'})
     vals['property_account_receivable_id'] = account_receivable_id
     return super().create(vals)



