# Copyright (c) 2026, sowmya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class SparePart(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		compatible_device_type: DF.Link | None
		is_active: DF.Check
		part_code: DF.Data
		part_name: DF.Data
		reorder_level: DF.Float
		selling_price: DF.Currency
		stock_qty: DF.Float
		unit_cost: DF.Currency
	# end: auto-generated types

	def validate(self):
		if self.selling_price < self.unit_cost:
			frappe.throw("Selling Price must be greater than Unit Cost.")
   
	def autoname(self):
		self.name = f"{self.part_code.upper()}" + "-" + make_autoname("PART-.YYYY.-.####")
  

		