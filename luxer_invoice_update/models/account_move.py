from odoo import api, fields, models
from odoo.odoo.exceptions import UserError


class AccountMove(models.Model):

    _inherit = 'account.move'

    site_address = fields.Many2one('res.partner', string='Site Address')



