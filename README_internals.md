#### Run: frappe.db.sql("SHOW TABLES LIKE '%Job%'") and list what you see. Explain the tab prefix convention.

    'tabJob Card', 'tabScheduled Job Log', 'tabScheduled Job Type' was the output of the SQL query. The tab prefix was added to a table in schema.py file which was added to the table name for the corresponding created doctype, it helps to avoid conflicts arise between Doctype names and SQL keywords.

____
#### Run: frappe.db.sql("DESCRIBE `tabJob Card`", as_dict=True) and list 5 column names you recognise from your DocType fields

Customer Name, Assigned Technician, Priority, Parts total, Payment Status.

____
#### What are the three numeric values of docstatus and what state does each represent?

The docstatus has 3 state of a doctype, it includes
0 - Draft
1 - Submit
2 - Cancel

____
#### What is the DB table name for the Part Usage Entry DocType?

`tabPart Usage Entry` is the DB table name of the doctype Part Usage Entry.

___
#### 

