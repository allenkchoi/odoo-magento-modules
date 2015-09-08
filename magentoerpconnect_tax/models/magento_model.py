# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
#    Coded by: Borni DHIFI  (dhifi.borni@gmail.com)
#
#-------------------------------------------------------------------------------

from openerp import models, api


class MagentoBackend(models.Model):
    _inherit = 'magento.backend'

    @api.model
    def select_versions(self):
        """ Available versions in the backend. """
        versions = super(MagentoBackend, self).select_versions()
        versions.append(('magento-custom', 'New Version'))
        return versions
