# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#
#    Coded by: Borni DHIFI  (dhifi.borni@gmail.com)
#
#-------------------------------------------------------------------------------

{
    'name': 'Magento Connector Synch  Tax',
    'version': '1.0',
    'category': 'Connector',
    'description': """
         Map tax in import product from magento.
    """,
    'author': 'Borni DHIFI',
    'depends': [ 'magentoerpconnect', 'account' ],
    'data': ['view/account_tax_view.xml',],
    'installable': True,
    'active': False,
}
