from repair_service import RepairService


class SoftwareRepair(RepairService):

    def __init__(self, service_id, name, labor_cost, status, license_key, os_version):
        super().__init__(service_id, name, labor_cost, status)

        self.license_key = license_key
        self.os_version = os_version

    def calculate_service_cost(self):
        digital_processing_fee = 5
        total = self.get_labor_cost() + digital_processing_fee
        return total

    def display_service_info(self):
        print(f"""
Service ID: {self._service_id}
Service Name: {self._name}
Type: Software Repair
License Key: {self.license_key}
OS Version: {self.os_version}
Status: {self.get_status()}
Labor Cost: ${self.get_labor_cost()}
""")