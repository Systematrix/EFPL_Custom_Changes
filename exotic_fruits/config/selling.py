from frappe import _

def get_data():
	return [
		{
			"label": _("Export Documents"),
			"icon": "icon-list",
			"items": [
				{
					"type": "doctype",
					"name": "Bank Set Of Documents",
					"description": _("Bank Set Of Documents, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Nutrition Certificate",
					"description": _("Nutrition Certificate, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Certificate Of Authenticity And Conformity",
					"description": _("Certificate Of Authenticity And Conformity, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Certificate Of Naturalness",
					"description": _("Certificate Of Naturalness, Export Document"),
				},
				{
					"type": "doctype",
					"name": "GMO DECLARATION",
					"description": _("GMO DECLARATION, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Shelf Life Certificate",
					"description": _("Shelf Life Certificate, Export Document"),
				},
				{
					"type": "doctype",
					"name": "DRUM MANIFEST",
					"description": _("DRUM MANIFEST, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Health Certificate",
					"description": _("Health Certificate, Export Document"),
				},
				{
					"type": "doctype",
					"name": "CARTON MANIFEST",
					"description": _("CARTON MANIFEST, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Shipment Advice",
					"description": _("Shipment Advice, Export Document"),
				},
				{
					"type": "doctype",
					"name": "Bill Of exchange",
					"description": _("Bill Of exchange, Export Document"),
				},
			]
		},
			{
			"label": _("Export Documents Factory"),
			"icon": "icon-list",
			"items": [
				{
					"type": "doctype",
					"name": "Invoice",
					"description": _("Factory Invoice. Factory Export Document"),
				},
				]
		},
	]
