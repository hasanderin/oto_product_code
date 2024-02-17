# -*- coding: utf-8 -*-
# Copyright (C) 2023 Quanimo (https://www.quanimo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    'name': "Quanimo Soluti Product",
    'summary': """Quanimo Soluti Product""",
    'description': """Quanimo Soluti Product""",
    'author': 'Quanimo',
    'company': 'Quanimo',
    'maintainer': 'Quanimo',
    'website': 'https://www.quanimo.com',
    'category': 'Sales/Sales',
    "version": "16.0.1.0.0",
    'sequence': 1453,
    'depends': ['purchase', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/update_sale_price_wizard.xml',
        'views/purchase_views.xml',
        'views/product_sequence_view.xml',
        'views/product_views.xml',
    ],
    "license": "LGPL-3",
    'installable': True,
    'application': False,
}
