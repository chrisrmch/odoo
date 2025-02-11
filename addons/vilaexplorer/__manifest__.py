# -*- coding: utf-8 -*-
{
    'name': "vilaexplorer",

    'summary': """
        Aplicación de Odoo para la gestión de de una aplicación de turismo """,

    'description': """
        Aplicación Odoo para la gestión de una aplicación orientada al turismo de La Vila Joyosa, Alicante
    """,

    'author': "Bug Busters",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'views/views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view_vilaexplorer.xml',
        'report/report_platos.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}