# -*- coding: utf-8 -*-
# Copyright (C) 2023 Quanimo (https://www.quanimo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sequence_id = fields.Many2one('ir.sequence', domain=[('code', 'ilike', 'product.product.default_code')],
                                  string='Sequence')
    stock_code = fields.Char('Stock Code')
    list_price_change_date = fields.Date()
    price_rate = fields.Float('List Price Rate')

    @api.depends('product_variant_ids', 'product_variant_ids.price_rate')
    def _compute_price_rate(self):
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.price_rate = template.product_variant_ids.price_rate
        for template in (self - unique_variants):
            template.price_rate = False

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if 'sequence_id' in val and val.get('sequence_id') and not val.get('stock_code', False):
                seq_rec = self.env['ir.sequence'].browse(val['sequence_id'])
                val['stock_code'] = self.env['ir.sequence'].next_by_code(seq_rec.code)

        return super(ProductTemplate, self).create(vals_list)

    def write(self, vals):
        default_code = vals.get('stock_code', self.stock_code)
        sequence_id = vals.get('sequence_id', self.sequence_id and self.sequence_id.id or False)

        if not default_code and sequence_id:
            seq_rec = self.env['ir.sequence'].browse(sequence_id)
            vals['stock_code'] = self.env['ir.sequence'].next_by_code(seq_rec.code)

        if 'list_price' in vals:
            vals['list_price_change_date'] = fields.Date.today()

        return super(ProductTemplate, self).write(vals)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    sequence_id = fields.Many2one('ir.sequence', related='product_tmpl_id.sequence_id',
                                  string='Sequence')
    stock_code = fields.Char('Stock Code', related='product_tmpl_id.stock_code')
    price_rate = fields.Float('List Price Rate')
