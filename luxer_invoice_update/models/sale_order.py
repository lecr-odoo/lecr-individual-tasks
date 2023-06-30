from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    site_address = fields.Many2one('res.partner', string='Site Address')

    def action_invoice_subscription(self):
        if self.site_address:
            account_move = self._create_recurring_invoice()
            if account_move:
                account_move.site_address = self.site_address
                return self.action_view_invoice()
            else:
                raise UserError(self._nothing_to_invoice_error_message())
        else:
            super(SaleOrder, self).action_invoice_subscription()
