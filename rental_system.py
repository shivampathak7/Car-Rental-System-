from car import Car
from customer import Customer


class RentalSystem:
    def __init__(self):
        self._cars = {}

    def add_car(self, car: Car):
        self._cars[car.car_id] = car

    def list_available_cars(self):
        return [c for c in self._cars.values() if c.available]

    def rent_car(self, customer: Customer, car_id: int, days: int):
        car = self._cars.get(car_id)

        if not car:
            raise ValueError("Invalid car ID")

        if not car.available:
            raise Exception("Car not available")

        car.mark_unavailable()
        total_cost = car.rate_per_day * days

        return {
            "customer": customer.name,
            "car": car.model,
            "days": days,
            "total_cost": total_cost
        }

    def return_car(self, car_id: int):
        car = self._cars.get(car_id)

        if not car:
            raise ValueError("Invalid car ID")

        if car.available:
            raise Exception("Car is already available")

        car.mark_available()
