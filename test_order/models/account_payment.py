# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class AccountPayment(models.Model):
    _inherit = 'account.payment'

