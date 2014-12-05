# Copyright (c) 2013, Systematrix and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Local Sale Invoice')

class TestLocalSaleInvoice(unittest.TestCase):
	pass
