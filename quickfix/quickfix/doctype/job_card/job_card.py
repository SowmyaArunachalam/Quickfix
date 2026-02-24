# Copyright (c) 2026, sowmya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class JobCard(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from quickfix.quickfix.doctype.part_usage_entry.part_usage_entry import PartUsageEntry

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
		naming_series: DF.Literal["JC-.YYYY.-.#####"]
		parts_total: DF.Currency
		party_usage_entry: DF.Table[PartUsageEntry]
		payment_status: DF.Literal["Unpaid", "Paid"]
		priority: DF.Literal["Normal", "High", "Urgent"]
		problem_description: DF.TextEditor
		remarks: DF.SmallText | None
		status: DF.Literal["Draft", "Pending Diagnosis", "Awaiting Customer Approval", "In Repair", "Ready for Delivery", "Delivered", "Cancelled"]
	# end: auto-generated types

	pass
