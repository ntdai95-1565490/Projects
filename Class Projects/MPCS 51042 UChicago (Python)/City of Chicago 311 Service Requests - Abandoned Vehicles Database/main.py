"""
The City of Chicago 311 Service Requests - Abandoned Vehicles Database you are creating is a searchable database that, given a csv file of 311 abandoned vehicles service requests data, can perform
data searches. All data results should be able to be displayed to the terminal, output to a csv file, or output to a plot.

Search Requirements:

1. By limit (e.g. get first 10)
2. By date or between a start date and end date, only valid dates should be supported
3. By ward
4. By status (e.g. open, completed)
5. By vehicle details including: make, model, color, and plates of the car.

To achieve this functionality the project should include Python objects that represent:
- 311 abandoned vehicle service request
- Vehicle
- A container object for the 311 abandoned vehicle service requests and vehicles
- An object to perform the data search on the container
- An object to write the output format of the search results

Example for how to use the program:

1. Searching by date: Find up to ten (10) 311 abandoned vehicles service requests on Jan 1, 2020 displaying output to terminal

`./main.py display --n 10 --date 2020-01-01`

2. Searching by ward and date: Find up to ten (10) 311 abandoned vehicles service requests between Jan 1, 2020 and Jan 10, 2020 within Ward 2,
exporting the results to a csv file

`./main.py csvfile --n 10 --start_date 2020-01-01 --end_date 2020-01-10 --ward 2`

3. Searching by date, ward and status: Find all completed 311 abandoned vehicles service requests between Jan 1, 2020 and Jan 10, 2020 within Ward 2,
exporting the results to a csv file

`./main.py csvfile --start_date 2020-01-01 --end_date 2020-01-10 --ward 2 --status completed`

3. Searching by date and car details: Find all 311 abandoned vehicles service requests between Jan 1, 2020 and Jan 10, 2020 of blue Acura vehicles,
exporting the results to plot chart

`./main.py plot --start_date 2020-01-01 --end_date 2020-01-10 --make Acura --color blue`

4. Searching by date and car details: Find all 311 abandoned vehicles service requests between Jan 1, 2020 and Jan 10, 2020 of vehicles with unknown plates,
exporting the results to plot chart

`./main.py plot --start_date 2020-01-01 --end_date 2020-01-10 --plate UNKNOWN`
"""


import argparse
import datetime
from models import ServiceRequest, Vehicle
from database import ServiceRequestDatabase
from search import ServiceRequestSearcher
from writer import ServiceRequestWriter


def user_input_parsing_out():
    parser = argparse.ArgumentParser(prog = "Commandline Interface", formatter_class = argparse.RawTextHelpFormatter, description = "Program to take in commandline arguments from the user")
    parser.add_argument("output", type = str, nargs = 1, choices = ["display", "csvfile", "plot"],
                        help = """Output
display      Displaying the user request to the terminal.
csvfile      Exporting the results matching with the user request to a csv file.
plot         Exporting the results matching with the user request to a plot chart.""")
    parser.add_argument("--n", help = "Returning the maximum number of matched results. If not given, then returning all the matched results.")
    parser.add_argument("--date", type = lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"), help = "Returning the results that matches the specified creation date")
    parser.add_argument("--start_date", type = lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"), help = "Returning the results that matches the specified start creation date")
    parser.add_argument("--end_date", type = lambda x: datetime.datetime.strptime(x, "%m/%d/%Y"), help = "Returning the results that matches the specified end creation date, inclusive")
    parser.add_argument("--ward", help = "Returning the results that matches the specified ward")
    parser.add_argument("--status", help = "Returning the results that matches the specified case status")
    parser.add_argument("--make", help = "Returning the results that matches the specified car make")
    parser.add_argument("--color", help = "Returning the results that matches the specified car color")
    parser.add_argument("--plate", help = "Returning the results that matches the specified car plate")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # TODO: Implement the command line interface
    args = user_input_parsing_out()

    # Load Data
    db = ServiceRequestDatabase(filename = 'data/311_abandoned_services.csv')
    db.load_data()

    # Get Results
    results = ServiceRequestSearcher(db).get_service_requests(
        filters = [args.n, args.date, args.start_date, args.end_date, args.ward, args.status, args.make, args.color, args.plate]  # TODO: Will need to retrieve from the command line interface
    )

    # TODO: What if there are no results?
    if results == []:
        print("There is no service request that matches all of the criteria inputs. Please, try to search with other requirements.")

    # Output Results
    ServiceRequestWriter().write(
        data = results,
        format = args.output[0]   # TODO: Will need to retrieve from the command line interface
    )
