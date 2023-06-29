{
    "name": "Automation for Employee's Birthday Template",

    "summary": " The company wants to automate sending an email template for their employees on their Birthday.",

    "description": """
     The company wants to automate sending an email template for their employees on their Birthday.
    """,

    "version": "0.1",

    "category": "Individual Tasks",

    "license": "OPL-1",

    "depends": ["hr","mail"],

    'data': [
        'data/birthday_email_template.xml',
        'data/ir_cron_data_birthday.xml',
    ],

    "author": "lecr",

    "website": "www.odoo.com",

    "application": True,

}
