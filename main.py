from rental_system import RentalSystem
from car import Car
from customer import Customer


def display_menu():
    print("\n--- Car Rental System ---")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")


def main():
    system = RentalSystem()

    system.add_car(Car(1, "Thar", 3000))
    system.add_car(Car(2, "Creta", 2500))
    system.add_car(Car(3, "Swift", 1500))

    while True:
        display_menu()

        try:
            choice = int(input("Select option: "))

            if choice == 1:
                cars = system.list_available_cars()
                if not cars:
                    print("No cars available")
                else:
                    for car in cars:
                        print(f"{car.car_id} | {car.model} | ₹{car.rate_per_day}/day")

            elif choice == 2:
                name = input("Enter name: ").strip()
                car_id = int(input("Car ID: "))
                days = int(input("Days: "))

                customer = Customer(name)
                receipt = system.rent_car(customer, car_id, days)

                print("\nBooking Confirmed")
                print(f"Customer : {receipt['customer']}")
                print(f"Car      : {receipt['car']}")
                print(f"Days     : {receipt['days']}")
                print(f"Amount   : ₹{receipt['total_cost']}")

            elif choice == 3:
                car_id = int(input("Car ID to return: "))
                system.return_car(car_id)
                print("Car returned successfully")

            elif choice == 4:
                print("Exiting system...")
                break

            else:
                print("Invalid option")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
