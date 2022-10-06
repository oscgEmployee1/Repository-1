# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def multi_create_invoice(selfs):
        new_account_moves = selfs.env['account.move']
        action = selfs.action_create_invoice()

        if action.get('res_id'):
            move_ids = [action['res_id']]
        elif action.get('domain'):
            move_ids = eval(action['domain'])[0][2]

        new_account_moves |= new_account_moves.browse(move_ids)

        return selfs.action_view_invoice(new_account_moves)

