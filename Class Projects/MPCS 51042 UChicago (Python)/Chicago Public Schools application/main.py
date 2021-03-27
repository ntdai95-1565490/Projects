from math import asin, sin, cos, sqrt, radians, degrees
import csv
from webbrowser import open_new_tab

# Radius of Earth in miles
EARTH_RADIUS = 3961


class School:
    """Attribute:
    id - School ID of the school as an integer
    name - Short Name of the school as a string
    network - Network in which the school is operated as a string
    address - street address of the school as a string
    zip - Zip code of the school as a string
    phones - Phone number of the school as a string
    grades - grades, which are taught at the school as a list of strings
    location - coordinate of the school as radians required by the instance of Coordinate Class"""


    def __init__(self, data):
        """Initializing the id, name, network, address, zip, phones, grades, and location attributes of the School class as specified in 
        the exercise"""


        self.id = int(data["School_ID"])
        self.name = data["Short_Name"]
        self.network = data["Network"]
        self.address = data["Address"]
        self.zip = data["Zip"]
        self.phones = data["Phone"]
        self.grades = data["Grades"].replace(" ","").split(",")
        self.location = from_degrees(float(data["Lat"]), float(data["Long"]))


    def __repr__(self):
        """Creating the string representation of the instances of the School class for the examples given by the exercise"""


        return f"School({self.name})"


    def open_website(self):
        """Passing the school's id to url to open the school's info webpage"""


        open_new_tab(f"http://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId={self.id}")


    def distance(self, coord):
        """Calculating the distance from the instance of the Coordinate class to the school's location, using the formula given in
        the exercise"""


        coord_latitude = coord.latitude
        coord_longitude = coord.longitude
        school_latitude = self.location.latitude
        school_longitude = self.location.longitude
        distance = 2 * EARTH_RADIUS * asin(sqrt(sin((coord_latitude - school_latitude) / 2) ** 2 + cos(coord_latitude) * cos(school_latitude) * sin((coord_longitude - school_longitude) / 2) ** 2))
        return distance


    def full_address(self):
        """Creating the multiline string representation of the schools full address. Note that the data is from the Chicago Public 
        Schools, and thus, all school is located in Chicago, Illinois"""


        school_full_address = f"{self.address}\nChicago\nIllinois\n{self.zip}"
        return school_full_address


class Coordinate:
    """Attribute:
    latitude - latitude in radians
    longitude - longitude in radians"""


    def __init__(self, latitude, longitude):
        """Initializing latitude and longitude attributes as radians"""


        self.latitude = latitude
        self.longitude = longitude


    def __repr__(self):
        """Creating a string representation of the Coordinate class with latitude and longitude as degrees for the examples given by 
        the exercise"""


        coordinate_in_degrees = self.as_degrees()
        latitude_in_degrees = coordinate_in_degrees[0]
        longitude_in_degrees = coordinate_in_degrees[1]
        return f"Coordinate({latitude_in_degrees}, {longitude_in_degrees})"


    def distance(self, coord):
        """Using the given formula to calculate the distance from the current location to another location given by anothe instances of
        the Coordinate class"""


        coord_latitude = coord.latitude
        coord_longitude = coord.longitude
        distance = 2 * EARTH_RADIUS * asin(sqrt(sin((coord_latitude - self.latitude) / 2) ** 2 + cos(coord_latitude) * cos(self.latitude) * sin((coord_longitude - self.longitude) / 2) ** 2))
        return distance


    def as_degrees(self):
        """Converting latitude and longitude from degrees to radians and return them as a tuple"""


        latitude_in_degrees = degrees(self.latitude)
        longitude_in_degrees = degrees(self.longitude)
        coordinate_in_degrees = tuple([latitude_in_degrees, longitude_in_degrees])
        return coordinate_in_degrees


    def show_map(self):
        """Converting the latitude and longitude attributes from radians to degrees by calling the as_degrees() function and pass those
        coordinates into the url to open the google map with those coordinates"""


        coordinate_in_degrees = self.as_degrees()
        latitude_in_degrees = coordinate_in_degrees[0]
        longitude_in_degrees = coordinate_in_degrees[1]
        open_new_tab(f"http://maps.google.com/maps?q={latitude_in_degrees},{longitude_in_degrees}")


class CPS:
    """Attribute:

    schools - list of instances of the School class for each school listed in the schools.csv file"""


    def __init__(self, filename):
        """Reading data from the file and pass each row for each instances of the School class. Then, store each of those instances in 
        a list."""
        self.schools = []
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                instance_of_School = School(row)
                self.schools.append(instance_of_School)


    def nearby_schools(self, coord, radius=1.0):
        """Iterating through the list of School instances and call the distance method from the School class to get the distance from
        the current location and check if the schools is within the radius."""


        list_of_nearby_schools = []
        for instance_of_School in self.schools:
            distance = instance_of_School.distance(coord)
            if distance <= radius:
                list_of_nearby_schools.append(instance_of_School)
        return list_of_nearby_schools


    def get_schools_by_grade(self, *grades):
        """Iterating through the list of School instances and get those schools, which have all of the asked grades requirements 
        satisfied."""


        list_of_schools_by_grade = []
        for instance_of_School in self.schools:
            number_of_user_asked_grades_satisfied = 0
            for user_asked_grade in grades:
                if user_asked_grade in instance_of_School.grades:
                    number_of_user_asked_grades_satisfied += 1
            if number_of_user_asked_grades_satisfied == len(grades):
                list_of_schools_by_grade.append(instance_of_School)
        return list_of_schools_by_grade


    def get_schools_by_network(self, network):
        """Iterating through the list of School instances to get the school with the asked network."""


        list_of_schools_by_network = []
        for instance_of_School in self.schools:
            if network == instance_of_School.network:
                list_of_schools_by_network.append(instance_of_School)
        return list_of_schools_by_network


def from_degrees(latitude, longitude):
    """Converting laitude and longitude from radians to degrees as an instance of Coordinate class."""


    latitude_in_radians = radians(latitude)
    longitude_in_radians = radians(longitude)
    instance_of_Coordinate = Coordinate(latitude_in_radians, longitude_in_radians)
    return instance_of_Coordinate


if __name__ == "__main__":
    # Checking with examples from the exercise
    cps = CPS('schools.csv')
    print(cps.schools[:5])
    print([s for s in cps.schools if s.name.startswith('OR')])
    ace_tech = cps.schools[1]
    print(ace_tech.location)
    the_bean = from_degrees(41.8821512, -87.6246838)
    print(cps.nearby_schools(the_bean, radius=0.5))
    print(cps.get_schools_by_grade('PK', '12'))
    print(cps.get_schools_by_network('Contract'))
