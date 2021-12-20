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

def get_conditions(filters):
	conditions = {}

	if filters.start_date:
		conditions["start_date"] = filters.start_date
	if filters.end_date:
		conditions["End_date"] =filters.end_date
	
	return conditions


def get_data(filters):

	data = []
	conditions = get_conditions(filters)
	emp = frappe.db.get_all("Employee_payrole", fields=["id","name","start_date", "end_date"],
		 filters=conditions, order_by='id')
	
	for d in emp:
		row = {"start_date": d.start_date, "end_date": d.end_date,"id": d.id, "name":d.name }

		data.append(row)

	return data