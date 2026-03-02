// Copyright (c) 2026, sowmya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Job Card", {
	onload(frm) {
        frappe.db.get_single_value("QuickFix Settings", "default_labour_charge").then((value)=>{
            if (value){
                frm.set_value("labour_charge", value)
            }
        })
	},
});

frappe.ui.form.on("Part Usage Entry", {
    part: function (frm, cdt, cdn) {
		update_total_price(frm, cdt, cdn)
    },
    quantity: function (frm, cdt, cdn) {
		update_total_price(frm, cdt, cdn)
    },
    unit_price: function (frm, cdt, cdn){
        update_total_price(frm, cdt, cdn)
    }
})

function update_total_price(frm, cdt, cdn) {
    var row = locals[cdt][cdn];
    frappe.model.set_value(cdt, cdn, "total_price", row.quantity * row.unit_price)
}