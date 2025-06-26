# -*- coding: utf-8 -*-
{
    'name': "Tourgull Blog",

    'summary': """
        blog""",

    'description': """
        Tourgull Blog Module
    """,

    'author': "Razzak and Tanvir",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'as_rental', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        # ===========  Front End Pages  ===========
        'templates/blog.xml',
        'templates/blog_details.xml',

        # ===========  Back End Pages  ===========
        'views/blog_page_view.xml',
        'views/blog_view.xml',
        'views/tag_view.xml',
        'views/category_view.xml',

        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
