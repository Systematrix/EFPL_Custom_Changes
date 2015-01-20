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
					"name": "Commercial Invoice",
					"description": _("Commercial Invoice. Factory Export Document"),
				},
				{
					"type": "doctype",
					"name": "Packing List",
					"description": _("Packing List. Factory Export Document"),
				},
				{
					"type": "doctype",
					"name": "Excise Certificate",
					"description": _("Excise Certificate. Factory Export Document"),
				},
				{
					"type": "doctype",
					"name": "Loading Supervision Report",
					"description": _("Loading Supervision Report. Factory Export Document"),
				},
				{
					"type": "doctype",
					"name": "ANNEXTURE C1",
					"description": _("ANNEXTURE C1. Factory Export Document"),
				},
				{
					"type": "doctype",
					"name": "Certificate Of Analysis",
					"description": _("Certificate Of Analysis. Factory Export Document"),

				},
                {
                    "type": "doctype",
                    "name": "Bill Of Loading",
                    "description": _("Bill Of Loading. Factory Export Document"),
                },
				
				]
		},
			{
			"label": _("Local Sale Documents"),
			"icon": "icon-list",
			"items": [
				{
					"type": "doctype",
					"name": "Local Sale Invoice",
					"description": _("Local Sale Invoice. Local Sale Export Document"),
				},
				{
					"type": "doctype",
					"name": "Delivery Challan",
					"description": _("Delivery Challan. Local Sale Export Document"),
				},
				{
					"type": "doctype",
					"name": "Certificate Of Analysis",
					"description": _("Certificate Of Analysis. Local Sale Export Document"),

				},
				]
		},
	]

