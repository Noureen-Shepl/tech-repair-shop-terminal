class CustomerInvoice:

    def __init__(self):
        self.repairs = []

    def add_repair(self, repair):
        self.repairs.append(repair)
        print("Repair service added to invoice successfully!")

    def view_invoice(self):
        if not self.repairs:
            print("Invoice is empty.")
        else:
            print("\n========== Customer Invoice ==========")
            for repair in self.repairs:
                repair.display_service_info()

    def print_final_bill(self):
        if not self.repairs:
            print("Invoice is empty. No bill to print.")
        else:
            total_amount = 0

            print("\n========== Final Repair Bill ==========")

            for repair in self.repairs:
                repair.display_service_info()
                cost = repair.calculate_service_cost()
                print(f"Service Total: ${cost:.2f}")
                print("--------------------------------------")
                total_amount += cost

            print(f"Final Total Amount: ${total_amount:.2f}")
            print("Thank you for choosing our repair shop!")