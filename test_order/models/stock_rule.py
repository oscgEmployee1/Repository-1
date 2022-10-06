# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, company_id, values, partner):
        domain = super()._make_po_get_domain(company_id, values, partner)
        if values.get('mock_origin'):
            domain += (('mock_origin','=',values['mock_origin']),)
        return domain

    def _prepare_purchase_order(self, company_id, origins, values):
        po_values = super()._prepare_purchase_order(company_id, origins, values)
        po_values.update({'mock_origin':values[0].get('mock_origin')})
        return po_values

    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        mo_values = super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        mo_values.update({'mock_origin':values.get('mock_origin')})
        return mo_values
