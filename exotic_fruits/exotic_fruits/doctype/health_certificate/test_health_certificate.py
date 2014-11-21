# Copyright (c) 2013, Systematrix and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Health Certificate')

class TestHealthCertificate(unittest.TestCase):
	pass
