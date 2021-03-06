# -*- coding: utf-8 -*-
{
    'name': "gsp_hr_employee_date",

    'summary': """
        Nambah field date mulai masuk (hr.employee) dan mulai aktif (hr.contract)""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/payslip.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}