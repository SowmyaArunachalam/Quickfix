import frappe
from frappe.utils import now, add_days
# @frappe.whitelist()
# def get_job_summary():
#     return frappe.get_doc("Job Card", "JC-2026-00001")

@frappe.whitelist()
def get_overdue_jobs():
    from frappe.query_builder import DocType, Order
    JC = DocType("Job Card")
    result = frappe.qb.from_(JC).select(JC.name, JC.customer_name, JC.assigned_technician, JC.creation).where((JC.status.isin(["Pending Diagnosis","In Repair"])) & (JC.creation < add_days(now(), -7))).orderby(JC.creation, order=Order.asc).run(as_dict=True)

