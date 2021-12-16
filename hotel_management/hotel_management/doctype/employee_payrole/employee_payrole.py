# Copyright (c) 2021, ponnusamy and contributors
# For license information, please see license.txt

import frappe
from datetime import date , timedelta
import calendar
from frappe.model.document import Document

class Employee_payrole(Document):
	def validate(self):
		r={"Developer":1000,'HouseKeeping':500,'Intern':400,"HR":1500}
		self.basic_pay=r[self.role]
		sd=int(self.start_date[8:])
		sm=int(self.start_date[5:7])
		sy=int(self.start_date[:4])
		d=date(sy,sm,sd)
		dm=calendar.monthrange(d.year,d.month)[1]
		res=str(d+timedelta(days=dm-1))
		#frappe.throw(res+'  '+res[8:]+'-'+res[5:7]+'-'+res[:4]+'  '+self.end_date)
		if(self.end_date==None):
			self.end_date=res
		
		ed=int(self.end_date[8:])
		em=int(self.end_date[5:7])
		ey=int(self.end_date[:4])
		e=date(ey,em,ed)
		if((e-d).days <0):
			frappe.throw("End date is less than start date")
		
