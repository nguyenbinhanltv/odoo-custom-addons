# -*- coding: utf-8 -*-
{
    'name': "Employees Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_bhxh_family_views.xml',
        'views/employee_bhxh_views.xml',
        'views/employee_friend_ref_views.xml',
        'views/employee_friend_views.xml',
        'views/employee_software_views.xml',
        'views/employee_language_views.xml',
        'views/employee_family_views.xml',
        'views/views.xml',
        'report/employee_management_badge.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
