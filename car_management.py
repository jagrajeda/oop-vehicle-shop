class CarManager:
    """
    Manages vehicle inventory, service records, and fleet totals.
    Demonstrates class attributes vs instance attributes and class methods vs instance methods.
    """

    # Class attributes shared across all instances
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage):
        """
        Initializes an individual Car instance.
        Increments class counter and assigns an auto-incrementing ID.
        """
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        self._make = make
        self._model = model
        self._year = int(year)
        self._mileage = int(mileage)
        self._services = []

        # Keep track of instance in the class-level registry
        CarManager.all_cars.append(self)

    @classmethod
    def get_total_cars(cls):
        """Class method returning the total number of cars registered."""
        return cls.total_cars

    @classmethod
    def find_car_by_id(cls, car_id):
        """Class method to query an instance from the fleet registry by unique ID."""
        for car in cls.all_cars:
            if car._id == car_id:
                return car
        return None

    def add_service(self, service_description):
        """Instance method appending a maintenance task to this vehicle's service history."""
        self._services.append(service_description)

    def update_mileage(self, new_mileage):
        """
        Instance method to update vehicle mileage.
        Prevents rolling back an odometer to a lower value.
        """
        if int(new_mileage) >= self._mileage:
            self._mileage = int(new_mileage)
        else:
            print("New mileage cannot be less than current mileage.")

    def get_details(self):
        """Instance method returning a formatted summary of vehicle specifications and service log."""
        services_list = ", ".join(self._services) if self._services else "No services recorded"
        return f"ID: {self._id} | {self._year} {self._make} {self._model} | Mileage: {self._mileage} | Services: {services_list}"


def terminal_app():
    """Terminal UI loop for interacting with the CarManager class."""
    while True:
        print("\n---- WELCOME ----")
        print("1. Add a car")
        print("2. View all cars")
        print("3. View total number of cars")
        print("4. See a car's details")
        print("5. Service a car")
        print("6. Update mileage")
        print("7. Quit")

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            mileage = input("Enter mileage: ")
            CarManager(make, model, year, mileage)
            print("Car added successfully.")

        elif choice == "2":
            if not CarManager.all_cars:
                print("No cars in the system.")
            else:
                for car in CarManager.all_cars:
                    print(car.get_details())

        elif choice == "3":
            print(f"Total cars: {CarManager.get_total_cars()}")

        elif choice == "4":
            try:
                car_id = int(input("Enter car ID: "))
                car = CarManager.find_car_by_id(car_id)
                if car:
                    print(car.get_details())
                else:
                    print(f"Car with ID {car_id} not found.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "5":
            try:
                car_id = int(input("Enter car ID: "))
                car = CarManager.find_car_by_id(car_id)
                if car:
                    service = input("Enter service details: ")
                    car.add_service(service)
                    print("Service recorded.")
                else:
                    print(f"Car with ID {car_id} not found.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "6":
            try:
                car_id = int(input("Enter car ID: "))
                car = CarManager.find_car_by_id(car_id)
                if car:
                    new_miles = int(input("Enter new mileage: "))
                    car.update_mileage(new_miles)
                    print(f"Mileage updated to {car._mileage}.")
                else:
                    print(f"Car with ID {car_id} not found.")
            except ValueError:
                print("Please enter a valid numeric value.")

        elif choice == "7":
            print("Exiting application.")
            break
        else:
            print("Invalid selection. Please choose between 1 and 7.")


if __name__ == "__main__":
    terminal_app()