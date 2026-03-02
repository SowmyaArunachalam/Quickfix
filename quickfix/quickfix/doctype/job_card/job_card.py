# Copyright (c) 2026, sowmya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class JobCard(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from quickfix.quickfix.doctype.part_usage_entry.part_usage_entry import PartUsageEntry

		amended_from: DF.Link | None
		assigned_technician: DF.Link | None
		customer_email: DF.Data | None
		customer_name: DF.Data
		customer_phone: DF.Data
		delivery_date: DF.Date | None
		device_brand: DF.Data | None
		device_model: DF.Data | None
		device_type: DF.Link
		diagnosis_date: DF.Date | None
		diagnosis_notes: DF.TextEditor | None
		estimated_cost: DF.Currency
		final_amount: DF.Currency
		imei_or_serial: DF.Data | None
		labour_charge: DF.Currency
		parts_total: DF.Currency
		party_usage_entry: DF.Table[PartUsageEntry]
		payment_status: DF.Literal["Unpaid", "Paid"]
		priority: DF.Literal["Normal", "High", "Urgent"]
		problem_description: DF.TextEditor
		remarks: DF.SmallText | None
		status: DF.Literal["Draft", "Pending Diagnosis", "Awaiting Customer Approval", "In Repair", "Ready for Delivery", "Delivered", "Cancelled"]
	# end: auto-generated types

	def validate(self):
		if len(self.customer_phone) != 10:
			frappe.throw("Length of phone number must be 10")

		if self.status in ["In Repair", "Ready for Delivery", "Delivered"] and not self.assigned_technician:
			frappe.throw("Technician must be assigned for work order with {0} status.".format(frappe.bold(self.status)))
			
		total = 0
		for entry in self.party_usage_entry:
			entry.total_price = entry.quantity * entry.unit_price
			total += entry.total_price

		self.parts_total = total
	
		if not self.labour_charge:
			self.labour_charge = frappe.db.get_single_value("QuickFix Settings", "default_labour_charge")
  
		self.final_amount = self.parts_total + self.labour_charge
  
	def before_submit(self):
		if self.status != "Ready for Delivery":
			frappe.throw("The Job Card can only be submitted when its status is Ready for Delivery.")
   
		for entry in self.party_usage_entry:
			stock_qty = frappe.db.get_value("Spare Part", entry.part, "stock_qty" ) or 0
			if stock_qty < entry.quantity:
				frappe.throw(f"Unavailable stock quantity for {entry.part}")

	def on_submit(self):
		for entry in self.party_usage_entry:
			stock_qty = frappe.db.get_value("Spare Part", entry.part, "stock_qty")
			entry.stock_qty = frappe.db.set_value("Spare Part", entry.part, "stock_qty", stock_qty-entry.quantity) 
		# ignore_permissions=True can't be an argument of frappe.db.set_value() and it will not check user permission and not trigger ORM functions.
  
		frappe.get_doc({
			"doctype": "Service Invoice",
			"job_card": self.name,
			"labour_charge": self.labour_charge,
			"parts_total": self.parts_total,
			"total_amount": self.final_amount
		}).insert(ignore_permissions = True)