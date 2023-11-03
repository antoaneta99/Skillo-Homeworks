class Tenant:
    def __init__(self, tenant_name, contact_info, lease_start_date):
        self._tenant_name = tenant_name
        self.__contact_info = contact_info
        self.__lease_start_date = lease_start_date

    def display_tenant_info(self):
        print(f"Tenant Name: {self._tenant_name}")
        print(f"Contact Info: {self.__contact_info}")
        print(f"Lease Start Date: {self.__lease_start_date}")

    def update_contact_info(self, new_contact_info):
        self.__contact_info = new_contact_info

class Rent:
    def __init__(self, payment_amount, due_date):
        self.__payment_amount = payment_amount
        self.__due_date = due_date
        self.__payment_status = "Unpaid"

    def record_payment(self):
        self.__payment_status = "Paid"

    def check_payment_status(self):
        return self.__payment_status

class Apartment:
    def __init__(self, apartment_number, square_footage, rent_amount):
        self.apartment_number = apartment_number
        self.square_footage = square_footage
        self.rent_amount = rent_amount

    def display_apartment_details(self):
        print(f"Apartment Number: {self.apartment_number}")
        print(f"Square Footage: {self.square_footage} sq. ft.")
        print(f"Rent Amount: £{self.rent_amount} per month")

class TenantInformation:
    def __init__(self):
        self.tenants = []

    def add_tenant(self, tenant):
        self.tenants.append(tenant)

    def update_lease_history(self, tenant, lease_start_date):
        tenant.lease_start_date = lease_start_date

    def find_tenant_info(self, tenant_name):
        for tenant in self.tenants:
            if tenant._tenant_name == tenant_name:
                return tenant

class Policy:
    def __init__(self, policy_id, description, effective_date):
        self.__policy_id = policy_id
        self.description = description
        self.effective_date = effective_date

    def list_policies(self):
        print(f"Policy ID: {self.__policy_id}")
        print(f"Description: {self.description}")
        print(f"Effective Date: {self.effective_date}")

    def check_compliance(self):
        pass

class MaintenanceRequest:
    def __init__(self, request_id, description, date_reported):
        self._request_id = request_id
        self.description = description
        self.status = "Open"
        self._date_reported = date_reported

    def record_request(self):
        pass

    def update_status(self, status):
        self.status = status

    def list_open_requests(self):
        if self.status == "Open":
            return self


tenant1 = Tenant("Viktor Viktorov", "viktor99@gmail.com", "2023-01-01")
rent1 = Rent(1000, "2023-11-01")
apartment1 = Apartment(101, 800, 1000)
tenant_info = TenantInformation()
policy1 = Policy(1, "No pets allowed", "2023-01-01")
maintenance_request1 = MaintenanceRequest(1, "Broken window", "2023-10-15")


try:
    tenant_info.add_tenant(tenant1)
    tenant_info.update_lease_history(tenant1, "2023-01-15")
    tenant1.display_tenant_info()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    rent1.record_payment()
    print(f"Rent Payment Status: {rent1.check_payment_status()}")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    apartment1.display_apartment_details()
    policy1.list_policies()
except Exception as e:
    print(f"An error occurred: {e}")

try:
    maintenance_request1.record_request()
    maintenance_request1.update_status("Closed")
    open_requests = maintenance_request1.list_open_requests()
    if open_requests:
        print(f"Open Maintenance Request: Request ID {open_requests._request_id}")
    else:
        print("No open maintenance requests.")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    found_tenant = tenant_info.find_tenant_info("Rosen Rosenov")
    if found_tenant:
        found_tenant.display_tenant_info()
    else:
        print('Tenant not found.')
except Exception as e:
    print(f"An error occurred: {e}")

# tenant_info.add_tenant(tenant1)
# tenant_info.update_lease_history(tenant1, "2023-01-15")
#
#
# tenant1.display_tenant_info()
#
# rent1.record_payment()
# print(f"Rent Payment Status: {rent1.check_payment_status()}")
#
# apartment1.display_apartment_details()
# policy1.list_policies()
#
# maintenance_request1.record_request()
# maintenance_request1.update_status("Closed")
# open_requests = maintenance_request1.list_open_requests()
# if open_requests:
#     print(f"Open Maintenance Request: Request ID {open_requests._request_id}")
# else:
#     print("No open maintenance requests.")
#
#
# found_tenant = tenant_info.find_tenant_info("Rosen Rosenov")
# if found_tenant:
#     found_tenant.display_tenant_info()
# else:
#     print('Tenant not found.')

