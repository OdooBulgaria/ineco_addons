# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-Today INECO LTD,. PART. (<http://www.ineco.co.th>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
import time
from datetime import datetime

from openerp import tools
from openerp.osv import fields, osv
from openerp.tools import float_is_zero
from openerp.tools.translate import _

import openerp.addons.decimal_precision as dp
import openerp.addons.product.product

class product_template(osv.osv):
    
    _inherit = 'product.template'

    def create(self, cr, uid, vals, context=None):
        if 'default_code' in vals and vals['default_code'] and 'ean13' in vals and not vals['ean13']:
            ean13 = openerp.addons.product.product.sanitize_ean13(vals['default_code'])
            vals.update({'ean13': ean13})
        return super(product_template, self).create(cr, uid, vals, context)

    def write(self, cr, uid, ids, data, context=None):
        if 'default_code' in data and data['default_code']:
            ean13 = openerp.addons.product.product.sanitize_ean13(data['default_code'])
            data['ean13'] = ean13 
        result = super(product_template, self).write(cr, uid, ids, data, context=context)
        return result



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: