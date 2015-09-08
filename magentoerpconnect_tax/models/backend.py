# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
#    Coded by: Borni DHIFI  (dhifi.borni@gmail.com)
#
#-------------------------------------------------------------------------------

import openerp.addons.connector.backend as backend
import openerp.addons.magentoerpconnect.backend as magento_backend

magento_custom = backend.Backend(parent=magento_backend.magento1700,
                                    version='magento-custom')
