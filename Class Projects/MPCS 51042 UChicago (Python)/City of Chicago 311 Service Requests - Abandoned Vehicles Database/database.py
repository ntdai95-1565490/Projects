import pandas as pd
from models import Vehicle, ServiceRequest


class ServiceRequestDatabase:
    dataframe_of_relevant_data = None
    list_of_Vehicle_instances = []
    list_of_ServiceRequest_instances = []


    def __init__(self, filename):
        self.filename = filename


    def load_data(self):
        fields = ["Creation Date", "Status", "Service Request Number", "License Plate", "Vehicle Make/Model", "Vehicle Color", "Ward"]
        df = pd.read_csv(self.filename, skipinitialspace = True, usecols = fields)
        ServiceRequestDatabase.dataframe_of_relevant_data = df[~df.Status.str.contains("Dup")]

        for index, row in enumerate(ServiceRequestDatabase.dataframe_of_relevant_data.values):
            car_plate = row[3]
            car_make = row[4]
            car_color = row[5]
            instance_of_Vehicle = Vehicle(car_plate, car_make, car_color)
            ServiceRequestDatabase.list_of_Vehicle_instances.append(instance_of_Vehicle)
            service_request_number = row[2]
            start_date = row[0]
            case_status = row[1]
            ward = row[6]
            instance_of_ServiceRequest = ServiceRequest(car_plate, car_make, car_color, service_request_number, start_date, case_status, ward)
            ServiceRequestDatabase.list_of_ServiceRequest_instances.append(instance_of_ServiceRequest)
        
