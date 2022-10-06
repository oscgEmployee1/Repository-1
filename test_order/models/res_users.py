# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def search(cls, args, **kwargs):
        if cls._context.get('res_users_domain_replace_dict'):
            args = [cls._context['res_users_domain_replace_dict'].get(arg,arg) for arg in args]

        return super().search(args, **kwargs)

