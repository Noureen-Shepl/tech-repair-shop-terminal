from abc import ABC, abstractmethod


class RepairService(ABC):

    def __init__(self, service_id, name, labor_cost, status):
        self._service_id = service_id
        self._name = name
        self.__labor_cost = labor_cost
        self.__status = status

    # Getter for labor cost
    def get_labor_cost(self):
        return self.__labor_cost

    # Setter for labor cost with validation
    def set_labor_cost(self, cost):
        if cost > 0:
            self.__labor_cost = cost
        else:
            print("Invalid labor cost!")

    # Getter for status
    def get_status(self):
        return self.__status

    # Setter for status with validation
    def set_status(self, status):
        allowed_status = ["Pending", "In Progress", "Fixed"]

        if status in allowed_status:
            self.__status = status
        else:
            print("Invalid status!")

    @abstractmethod
    def calculate_service_cost(self):
        pass

    @abstractmethod
    def display_service_info(self):
        pass