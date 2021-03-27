import pandas as pd
import datetime


class ServiceRequestSearcher:
    list_of_ServiceRequest_instances = []


    def __init__(self, instance_of_ServiceRequestDatabase):
        self.instance_of_ServiceRequestDatabase = instance_of_ServiceRequestDatabase
        ServiceRequestSearcher.list_of_ServiceRequest_instances = self.instance_of_ServiceRequestDatabase.list_of_ServiceRequest_instances


    def get_service_requests(self, filters):
        if filters[1] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: filters[1] == datetime.datetime(int(x.start_date.split("/")[2]), int(x.start_date.split("/")[0]), int(x.start_date.split("/")[1])), ServiceRequestSearcher.list_of_ServiceRequest_instances))

        if filters[2] != None and filters[3] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: filters[2] <= datetime.datetime(int(x.start_date.split("/")[2]), int(x.start_date.split("/")[0]), int(x.start_date.split("/")[1])) <= filters[3], ServiceRequestSearcher.list_of_ServiceRequest_instances))

        if filters[4] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: float(filters[4]) == x.ward, ServiceRequestSearcher.list_of_ServiceRequest_instances))

        if filters[5] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: filters[5].capitalize() == x.case_status, ServiceRequestSearcher.list_of_ServiceRequest_instances))

        if filters[6] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: isinstance(x.car_make, str) and filters[6] in x.car_make, ServiceRequestSearcher.list_of_ServiceRequest_instances))
        
        if filters[7] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: filters[7].capitalize() == x.car_color, ServiceRequestSearcher.list_of_ServiceRequest_instances))
        
        if filters[8] != None:
            ServiceRequestSearcher.list_of_ServiceRequest_instances = list(filter(lambda x: filters[8].upper() == x.car_plate, ServiceRequestSearcher.list_of_ServiceRequest_instances))

        if filters[0] != None:
            return ServiceRequestSearcher.list_of_ServiceRequest_instances[:int(filters[0])]
        else:
            return ServiceRequestSearcher.list_of_ServiceRequest_instances