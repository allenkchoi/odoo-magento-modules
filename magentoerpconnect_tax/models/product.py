# -*- coding: utf-8 -*-


from openerp import models, fields, api, _
from openerp.addons.connector.unit.mapper import mapping
from openerp.addons.magentoerpconnect.product import ProductImportMapper
from .backend import magento_custom

    
class AccountTax(models.Model):
    _inherit = 'account.tax'
    
    magento_tax_id= fields.Integer(string='Magento Tax ID')

@magento_custom
class TaxProductImportMapper(ProductImportMapper):
    _model_name = 'magento.product.product'

    @mapping
    def tax_id(self, record):        
        tax_class_id = record.get('tax_class_id', '-1')       
        sess_obj = self.session
        tax_ids = sess_obj.search('account.tax',[('magento_tax_id','=',tax_class_id)])        
        result = {'taxes_id': [(6, 0, tax_ids)]}       
        return result
        