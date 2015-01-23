# Copyright (c) 2013, Systematrix and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Documents Required')

class TestDocumentsRequired(unittest.TestCase):
	pass
