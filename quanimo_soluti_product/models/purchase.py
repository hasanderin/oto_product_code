# -*- coding: utf-8 -*-
# Copyright (C) 2023 Quanimo (https://www.quanimo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def update_product_prices_wizard(self):
        self.ensure_one()

        ctx = {
            'default_update_line': []
        }

        for line in self.order_line:
            list_price = line.product_id.product_tmpl_id.list_price
            if line.product_id.price_rate > 0.0:
                list_price = line.product_id.product_tmpl_id.list_price + (
                            line.product_id.product_tmpl_id.list_price * line.product_id.price_rate / 100)

            ctx.get('default_update_line').append((0, 0, {
                'product_id': line.product_id.id,
                'rate': line.product_id.price_rate,
                'price': list_price
            }))

        action = {
            'name': _('Update Sale Price'),
            'view_mode': 'form',
            'res_model': 'update.sale.price.wizard',
            'view_id': self.env.ref('quanimo_soluti_product.update_sale_price_form').id,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'context': ctx
        }
        return action
