# See LICENSE file for full copyright and licensing details.
import os.path

import odoo, base64, tempfile
import zipfile
from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import datetime

class TestOrder(models.Model):
    _name = 'test.order'
    _inherit = ['mail.thread']

    name = fields.Char(translate=True)

    test_order_id = fields.Many2one('test.order')
    potential_test_order_ids = fields.Many2many('test.order','test_order_potential_test_order_rel','test_order_id','potential_test_order_id')

    c1 = fields.Char(inverse=False)
    f1 = fields.Float(inverse=False)
    f2 = fields.Float()

    @api.onchange('c1')
    def onchange_for_f1(self):
        self.f1 = self.c1


    def test(self):
        _zip = self.env['ir.attachment'].search([
            ('res_model','=',self._name),('res_id','=',self.id),('name','like','%.zip')],limit=1)

        with tempfile.TemporaryDirectory() as _directory_path:
            with open(os.path.join(tempfile.gettempdir(), _zip.name), 'wb') as _zip_file:
                _zip_file.write(base64.b64decode(_zip.datas))
                zip_object = zipfile.ZipFile(_zip_file.name)
                for attachment_name in zip_object.namelist():
                    attachment_path = zip_object.extract(attachment_name,_directory_path)
                    with open(attachment_path, 'rb') as attachment_file:
                        self.env['ir.attachment'].create({
                            'datas': base64.b64encode(attachment_file.read()),
                            'res_id': self.id,
                            'res_model': self._name,
                            'name': attachment_name,
                        })



