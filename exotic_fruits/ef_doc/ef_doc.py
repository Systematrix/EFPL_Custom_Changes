# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
import logging
import string
import datetime
import re
import json

from frappe.utils import getdate, flt,validate_email_add, cint
from frappe.model.naming import make_autoname
from frappe import throw, _, msgprint
import frappe.permissions
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

_logger = logging.getLogger(frappe.__name__)

@frappe.whitelist(allow_guest=True)
def apply_documents_required(self, method):
        doc_req = []
        if not self.documents_required and self.documents_required_master:
		doc_master = frappe.get_doc("Documents Required Master", self.documents_required_master)
		for value in doc_master.get("documents_required_master"):
			doc_req = {
				"doctype": "Documents Required",
				"name_of_document": value.name_of_document,
				"dispatch_address": value.dispatch_address,
                                "number_of_copies": value.number_of_copies,
                                "buyer": value.buyer,
                                "buyer_address": value.buyer_address,
				"consignee": value.consignee,
				"consignee_address": value.consignee_address,
                                "notify_party_i": value.notify_party_i,
                                "notify_party_ii": value.notify_party_ii,
                                "notify_party_iii": value.notify_party_iii,
                                "notify_party_address_i": value.notify_party_address_i,
                                "notify_party_address_ii": value.notify_party_address_ii,
				"notify_party_address_iii": value.notify_party_address_iii
			}
                        self.append("documents_required", doc_req)


			

