class Vehicle:
    def __init__(self, car_plate, car_make, car_color):
        self.car_plate = car_plate
        self.car_make = car_make
        self.car_color = car_color


    def __repr__(self):
        return f"The vehicle has a license plate of {self.car_plate}, a color of {self.car_color}, and made by {self.car_make}."


class ServiceRequest(Vehicle):
    def __init__(self, car_plate, car_make, car_color, service_request_number, start_date, case_status, ward):
        super().__init__(car_plate, car_make, car_color)
        self.service_request_number = service_request_number
        self.start_date = start_date
        self.case_status = case_status
        self.ward = ward


    def __repr__(self):
        return f"The service request number {self.service_request_number} is made on the Vehicle({self.car_plate}, {self.car_color}, {self.car_make}), starting on {self.start_date} with a case status of {self.case_status} in the {self.ward} ward."