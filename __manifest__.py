# -*- coding: utf-8 -*-
{
    'name': "Account Analytic Cost",

    'author': "César Gutierrez",

    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_pending'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}