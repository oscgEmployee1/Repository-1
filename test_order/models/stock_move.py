# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'


    def _prepare_procurement_values(self):
        values = super()._prepare_procurement_values()
        values['mock_origin'] = self._context.get('mock_origin')
        return values


    @api.model
    def create(cls, values):
        if cls._context.get('postrollback_mock_create'):
            values['group_id'] = False
        return super().create(values)

