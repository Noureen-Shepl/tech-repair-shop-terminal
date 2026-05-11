from repair_service import RepairService


class HardwareRepair(RepairService):

    def __init__(self, service_id, name, labor_cost, status, part_cost, warranty):
        super().__init__(service_id, name, labor_cost, status)

        self.part_cost = part_cost
        self.warranty = warranty

    def calculate_service_cost(self):
        tax = self.part_cost * 0.10
        total = self.get_labor_cost() + self.part_cost + tax
        return total

    def display_service_info(self):
        print(f"""
Service ID: {self._service_id}
Service Name: {self._name}
Type: Hardware Repair
Part Cost: ${self.part_cost}
Warranty: {self.warranty} months
Status: {self.get_status()}
Labor Cost: ${self.get_labor_cost()}
""")