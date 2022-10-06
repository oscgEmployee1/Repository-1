# See LICENSE file for full copyright and licensing details.

{
    'name': 'test_order',
    'depends': [
        'mail','hr','sale','purchase','stock'
    ],
    "version": "14.0",
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'views/menu.xml',
        'views/test_order.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
    'auto_install': False,
}
