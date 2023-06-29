from odoo import models, fields
from datetime import date


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def _send_birthday_email(self):
        # Fetch all the employees in the database
        employees = self.env['hr.employee'].search([])
        # Iterating through the employees
        for employee in employees:
            # Checking if the birthday and work email exists
            if employee.birthday and employee.work_email:
                # Checking if today matches with their birthday
                if employee.birthday.month == date.today().month and employee.birthday.day == date.today().day:

                    try:
                        # Rendering the email template
                        body_html = self.env['ir.qweb']._render(
                            'birthday_automation_template.birthday_email_template', {'employee': employee})
                        # Setting the mail values
                        mail_values = {
                            "subject": "Happy Birthday",
                            "email_from": "odoobot@odoo.com",
                            "email_to": employee.work_email,
                            "body_html": body_html,
                        }
                        # Create the email that needs to be sent out
                        mail = self.env['mail.mail'].sudo().create(mail_values)
                        mail.send(raise_exception=False)
                    except Exception as e:
                        print("Error while sending birthday email, please retry job")
                        print(e)


        # mail_template = self.env.ref('birthday_automation_template.birthday_email_template')
        # mail_template.send_mail(self.id, force_send=True)
        #
        # self_ctxt = self.with_context(lang=partner.lang)
        # product_ctxt = product.with_context(lang=partner.lang)
        # body_html = self_ctxt.env['ir.qweb']._render(
        #     'website_sale_stock.availability_email_body', {'product': product_ctxt})
        # msg = self_ctxt.env['mail.message'].sudo().new(dict(body=body_html, record_name=product_ctxt.name))
        # full_mail = self_ctxt.env['mail.render.mixin']._render_encapsulate(
        #     "mail.mail_notification_light",
        #     body_html,
        #     add_context=dict(message=msg, model_description=_("Product")),
        # )
        # context = {'lang': partner.lang}  # Use partner lang to translate mail subject below
        # mail_values = {
        #     "subject": _("The product '%(product_name)s' is now available", product_name=product_ctxt.name),
        #     "email_from": (product.company_id.partner_id or self.env.user).email_formatted,
        #     "email_to": partner.email_formatted,
        #     "body_html": full_mail,
        # }
        # del context
        #
        # mail = self_ctxt.env['mail.mail'].sudo().create(mail_values)
        # mail.send(raise_exception=False)

