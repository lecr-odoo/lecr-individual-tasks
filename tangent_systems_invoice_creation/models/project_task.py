from odoo import api, fields, models,_
from odoo.odoo.exceptions import ValidationError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    invoice_number = fields.Many2one(comodel_name="account.move", ondelete='restrict')
    delivery_date = fields.Date()

    @api.onchange('delivery_date')
    def _onchange_delivery_date_create_invoice(self):
        if self.delivery_date and self.sale_line_id:
            if self.sale_line_id.product_uom_qty > 1:
                raise ValidationError(_('The ordered quantity is more than 1.'))
            if self.sale_line_id.qty_delivered >= 1:
                raise ValidationError(_('There is already a delivered quantity of 1.'))
            else:
                self.sale_line_id.qty_delivered = 1
                draft_invoice = self.sale_order_id._create_invoices(self)
                self.invoice_number = int(draft_invoice)
