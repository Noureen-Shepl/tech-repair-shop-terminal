from hardware_repair import HardwareRepair
from software_repair import SoftwareRepair
from customer_invoice import CustomerInvoice


invoice = CustomerInvoice()


services = [
    HardwareRepair(1, "Screen Replacement", 50, "Pending", 100, 6),
    HardwareRepair(2, "Battery Replacement", 40, "Pending", 60, 3),

    SoftwareRepair(3, "Windows Installation", 30, "Pending", "WIN-12345", "Windows 11"),
    SoftwareRepair(4, "Virus Removal", 25, "Pending", "SAFE-67890", "Windows 10")
]


while True:

    print("""
========== Tech Repair Shop ==========
1. View Services
2. Add Service to Invoice
3. View Invoice
4. Print Final Bill
5. Exit
""")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("\n========== Available Services ==========")

            for service in services:
                service.display_service_info()

        elif choice == 2:

            service_id = int(input("Enter Service ID: "))

            found = False

            for service in services:

                if service._service_id == service_id:
                    invoice.add_repair(service)
                    found = True
                    break

            if not found:
                print("Service not found!")

        elif choice == 3:

            invoice.view_invoice()

        elif choice == 4:

            invoice.print_final_bill()

        elif choice == 5:

            print("Exiting system...")
            break

        else:
            print("Invalid choice! Please choose from 1 to 5.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")