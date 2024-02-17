# -*- coding: utf-8 -*-
# Copyright (C) 2023 Quanimo (https://www.quanimo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import api, models


class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    @api.model
    def create(self, vals_list):
        res = super(IrSequence, self).create(vals_list)
        if res['code'] == 'product.product.default_code':
            sequence = self.env['ir.sequence'].next_by_code('product.sequence.action')
            res['code'] = "%s_%s" % (res['code'], sequence)
        return res
