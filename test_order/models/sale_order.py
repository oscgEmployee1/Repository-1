# See LICENSE file for full copyright and licensing details.
import odoo
from odoo import fields, models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    note1 = fields.Char()

    def mock_action_confirm(self):
        self.with_context(mock_origin=self.name).action_confirm()

        self.env.cr.prerollback.add(self.prerollbcak_add_mock_records)
        self.env.cr.postrollback.add(self.postrollbcak_add_mock_records)

        self.env.cr.rollback()



    mock_purchase_ids = fields.Many2many('purchase.order','sale_order_mock_purchase_order_rel',copy=False)
    mock_production_ids = fields.Many2many('mrp.production','sale_order_mock_mrp_production_rel',copy=False)

    def prerollbcak_add_mock_records(self):
        mock_purchase_orders = self.env['purchase.order'].search([('mock_origin', '=', self.name)])
        mock_purchase_order_values_list = [each.copy_data({'state':'cancel'}) for each in mock_purchase_orders]

        mock_mrp_productions = self.env['mrp.production'].search([('mock_origin', '=', self.name)])
        mock_mrp_production_values_list = [each.copy_data({'state':'cancel'}) for each in mock_mrp_productions]

        self.env.cr.postrollback.data.update({
            'mock_purchase_order_values_list': mock_purchase_order_values_list,
            'mock_mrp_production_values_list': mock_mrp_production_values_list,
        })


    def postrollbcak_add_mock_records(self):
        self = self.with_context(postrollback_mock_create=True)

        for mock_purchase_order_values in self.env.cr.postrollback.data['mock_purchase_order_values_list']:
            self.mock_purchase_ids |= self.env['purchase.order'].create(mock_purchase_order_values)

        for mock_mrp_production_values in self.env.cr.postrollback.data['mock_mrp_production_values_list']:
            self.mock_production_ids |= self.env['mrp.production'].create(mock_mrp_production_values)

