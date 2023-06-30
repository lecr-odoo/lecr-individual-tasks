{
    "name": "Luxer Invoice Update",
    
    "summary": "Copy property from subscription to invoice delivery address",
    
    "description": """
    Copy property from subscription to invoice delivery address.
    """,
    
    "version": "0.1",
    
    "category": "Luxer",
    
    "license": "OPL-1",
    
    "depends": ["sale_management", "sale_subscription"],

    "data":[
        "views/sale_order_template_inherit.xml",
        "views/sale_order_form_inherit.xml",
        "views/account_view_move_form_inherit.xml"
    ],

    "author": "lecr",
    
    "website": "www.odoo.com",
    
    "application": True,
    
}