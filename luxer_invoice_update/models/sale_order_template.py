from odoo import api, fields, models

class SaleOrderTemplate(models.Model):

    _inherit = 'sale.order.template'

    property_partner = fields.Many2one('res.partner', string='Property Partner')


