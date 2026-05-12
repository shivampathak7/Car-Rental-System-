class Car:
    def __init__(self, car_id: int, model: str, rate_per_day: float):
        self.car_id = car_id
        self.model = model
        self.rate_per_day = rate_per_day
        self.available = True

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True
