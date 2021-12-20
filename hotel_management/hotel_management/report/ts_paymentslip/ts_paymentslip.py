# Copyright (c) 2013, ponnusamy and contributors
# For license information, please see license.txt

# import frappe
# get_data get_columns
from __future__ import unicode_literals
import datetime
import frappe
from frappe import _

def execute(filters=None):
	filters = frappe._dict(filters or {})
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data
def get_columns(filters):
	columns = [
		{
			"label": _("ID"),
			"fieldtype":"Data",
			"fieldname":"id"
		},
		{
			"label":_("Name"),
			"fieldtype":"Data",
			"fieldname":"name"
		},
		{
			"label": _("Start Date"),
			"fieldtype": "Date",
			"fieldname": "start_date"
		},
		{
			"label": _("End date"),
			"fieldtype": "Date",
			"fieldname": "end_date"
		}
		]
	return columns




def get_data(filters):

	data = []
	emp = frappe.db.get_all("Employee_payrole", fields=["id","name","start_date", "end_date"],
		  order_by='id')
	a=filters.start_date
	b=filters.end_date
	m=datetime.date( int(a[:4]),int(a[5:7]),int(a[8:]))
	n=datetime.date( int(b[:4]),int(b[5:7]),int(b[8:]))
	
	for d in emp:
		z=datetime.date( int(d.end_date[:4]),int(d.end_date[5:7]),int(d.end_date[8:]))

		if(d.start_date>=m and z<=n):
			row = {"start_date": d.start_date, "end_date": z,"id": d.id, "name":d.name }
			
			data.append(row)

	return data