import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime


class ServiceRequestWriter:
    def write(self, format, data):
        if format.lower() == "display":
            for instance_of_ServiceRequest in data:
                print(instance_of_ServiceRequest)
                
        elif format.lower() == "csvfile":
            dictionary_of_matching_service_request = {"Creation Date": [], "Status": [], "Service Request Number": [], "License Plate": [], "Vehicle Make/Model": [], "Vehicle Color": [], "Ward": []}
            for instance_of_ServiceRequest in data:
                dictionary_of_matching_service_request["Creation Date"].append(instance_of_ServiceRequest.start_date)
                dictionary_of_matching_service_request["Status"].append(instance_of_ServiceRequest.case_status)
                dictionary_of_matching_service_request["Service Request Number"].append(instance_of_ServiceRequest.service_request_number)
                dictionary_of_matching_service_request["License Plate"].append(instance_of_ServiceRequest.car_plate)
                dictionary_of_matching_service_request["Vehicle Make/Model"].append(instance_of_ServiceRequest.car_make)
                dictionary_of_matching_service_request["Vehicle Color"].append(instance_of_ServiceRequest.car_color)
                dictionary_of_matching_service_request["Ward"].append(instance_of_ServiceRequest.ward)

            df = pd.DataFrame(dictionary_of_matching_service_request)
            df.to_csv("matching_311_abandoned_services.csv", index = False)

        elif format.lower() == "plot":
            data.sort(key = lambda x: datetime.date(int(x.start_date.split("/")[2]), int(x.start_date.split("/")[0]), int(x.start_date.split("/")[1])))
            number_of_days = datetime.date(int(data[-1].start_date.split("/")[2]), int(data[-1].start_date.split("/")[0]), int(data[-1].start_date.split("/")[1])) - datetime.date(int(data[0].start_date.split("/")[2]), int(data[0].start_date.split("/")[0]), int(data[0].start_date.split("/")[1]))
            y_axis = []
            x_axis = []
            x_axis_datetime_format = [datetime.date(int(data[0].start_date.split("/")[2]), int(data[0].start_date.split("/")[0]), int(data[0].start_date.split("/")[1])) + datetime.timedelta(day) for day in range(number_of_days.days)]
            for date in x_axis_datetime_format:
                x_axis.append(date.strftime("%m/%d/%Y"))
                number_of_requests_per_day = sum(x.start_date.count(date.strftime("%m/%d/%Y")) for x in data)
                y_axis.append(number_of_requests_per_day)
            
            arr_x_axis = np.array(x_axis)
            arr_y_axis = np.array(y_axis)
            plt.title("311 abandoned vehicles service requests per day")
            plt.xlabel("date")
            plt.ylabel("number of 311 abandoned vehicles service requests")
            plt.plot(arr_x_axis, arr_y_axis)
            plt.show()