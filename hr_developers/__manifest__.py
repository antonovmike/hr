{
    'name': "HR Developers",
    'version': '16.0.1.0.0',
    'category': 'Human Resources',
    'summary': """Odoo test task""",
    'license': 'LGPL-3',
    'author': "Antonov Mike",
    'website': 'https://github.com/antonovmike',
    'depends': [
        'base', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/company_view.xml',
        'views/developers_view.xml',
        'views/developers_menu.xml',
    ],
    'demo': [],
    'images': [],
    'live_test_url': '',
    'price': 0,
    'currency': 'EUR',
    'support': '',
    'application': True,
    'installable': True,
    'auto_install': False,
}
