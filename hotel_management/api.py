import frappe
@frappe.whitelist(allow_guest=True)
def getname():
    a=frappe.get_all('TS_Parking')
    return a



#apps/hotel_management/hotel_management/api.py
#/home/thirvusoft/frappe-bench/apps/hotel_management/hotel_management/api.py