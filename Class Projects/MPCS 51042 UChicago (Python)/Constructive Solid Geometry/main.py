import tkinter as tk
import math # needed for the square root function below
from abc import ABC, abstractmethod
from csg_details import CANVAS_HEIGHT, CANVAS_WIDTH # created a separate python file to store constant variables related to the canvas


class Drawable(ABC):
    """Abstract Base Class for the Circle, Rectangle, Intersection, Union, and Difference subclasses below"""


    @abstractmethod
    def __contains__(self):
        """Abstract method for the Circle, Rectangle, Intersection, Union, and Difference subclasses below"""
        pass


    def __and__(self, other):
        """Overloading the & operator by calling the Intersection subclass"""


        instance_of_Intersection = Intersection(self, other)
        return instance_of_Intersection


    def __or__(self, other):
        """Overloading the | operator by calling the Union subclass"""


        instance_of_Union = Union(self, other)
        return instance_of_Union


    def __sub__(self, other):
        """Overloading the - operator by calling the Difference subclass"""


        instance_of_Difference = Difference(self, other)
        return instance_of_Difference


    def draw(self, canvas):
        """Iterating over each (x, y) pixels of canvas and if it's in the current subclass through the ABC of Drawable superclass, then
        call the draw_pixel() function. Note that we need reposition the center from the physical coordinates by adding half of canvas 
        width to x coordinate and half of canvas height to y coordinate."""


        for x in range(-int(int(canvas["width"]) / 2), int(int(canvas["width"]) / 2)):
            for y in range(-int(int(canvas["height"]) / 2), int(int(canvas["height"]) / 2)):
                if (x, y) in self:
                    draw_pixel(canvas, x + int(canvas["width"]) / 2, y + int(canvas["height"]) / 2)


class Circle(Drawable):
    """Representing circle type objects
    Attributes:
    x - x coordinate of the center of the circle
    y - y coordinate of the center of the circle
    r - radius of the circle"""


    def __init__(self, x, y, r):
        """Initializing the instance attributes of the circle center's x and y coordinates and the circle's radius, r"""


        self.x = x
        self.y = y
        self.r = r


    def __contains__(self, point):
        """Checking if the point is in the circle by calculating the distance between the center of the circle and the point and if 
        the distance is less than or equal to the radius, then the point is in the circle, otherwise it is outside of the circle"""


        point_x_coord = point[0]
        point_y_coord = point[1]
        distance = math.sqrt((point_x_coord - self.x) ** 2 + (point_y_coord - self.y) ** 2)

        if distance <= self.r:
            return True
        else:
            return False


    def __repr__(self):
        """Creating a string representaion of the circle for the user as asked in the exercise"""


        return f"The circle's center is located at ({self.x}, {self.y}) and has a radius of {self.r}."


class Rectangle(Drawable):
    """Representing rectangle type objects
    Attributes:
    x0 - x coordinate of the lower-left corner of the rectangle
    y0 - y coordinate of the lower-left corner of the rectangle
    x1 - x coordinate of the upper-right corner of the rectangle
    y1 - y coordinate of the upper-right corner of the rectangle"""


    def __init__(self, x0, y0, x1, y1):
        """Initializing the instance attributes of the rectangle's lower-left and upper-right corners' x and y coordinates"""


        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1


    def __contains__(self, point):
        """Checking if the point is in the rectangle by checking if the point's x coordinate is between the x coordinates of the 
        lower-left and uppper-right corners and if the point's y coordinate is between the y coordinates of the lower-left and 
        uppper-right corners, otherwise the point is outside the rectangle"""


        point_x_coord = point[0]
        point_y_coord = point[1]
        if self.x0 <= point_x_coord <= self.x1 and self.y1 <= point_y_coord <= self.y0:
            return True
        else:
            return False


    def __repr__(self):
        """Creating a string representaion of the rectangle for the user as asked in the exercise"""


        return f"The rectangle has a lower-left corner at ({self.x0}, {self.y0}) and upper-right corner at ({self.x1}, {self.y1}). It has a width of {self.x1 - self.x0} and height of {self.y0 - self.y1}."


class Intersection(Drawable):
    """Representing intersection of two objects
    Attributes:
    shape1 - shape of the first object
    shape2 - shape of the second object"""


    def __init__(self, shape1, shape2):
        """Initializing the instance attributes of the shapes of the first and second objects"""


        self.shape1 = shape1
        self.shape2 = shape2


    def __contains__(self, point):
        """Checking if the point is in both of the shapes of objects or not"""


        if point in self.shape1 and point in self.shape2:
            return True
        else:
            return False


    def __repr__(self):
        """Creating a string representaion of the intersection for the user as asked in the exercise"""


        return f"Intersecion of {self.shape1} and {self.shape2}."


class Union(Drawable):
    """Representing union of two objects
    Attributes:
    shape1 - shape of the first object
    shape2 - shape of the second object"""


    def __init__(self, shape1, shape2):
        """Initializing the instance attributes of the shapes of the first and second objects"""


        self.shape1 = shape1
        self.shape2 = shape2


    def __contains__(self, point):
        """Checking if the point is in at least one of the shapes of objects or not"""


        if point in self.shape1 or point in self.shape2:
            return True
        else:
            return False


    def __repr__(self):
        """Creating a string representaion of the union for the user as asked in the exercise"""


        return f"Union of {self.shape1} and {self.shape2}."


class Difference(Drawable):
    """Representing difference of two objects
    Attributes:
    shape1 - shape of the first object
    shape2 - shape of the second object"""


    def __init__(self, shape1, shape2):
        """Initializing the instance attributes of the shapes of the first and second objects"""


        self.shape1 = shape1
        self.shape2 = shape2


    def __contains__(self, point):
        """Checking if the point is in the shape of the first object but not in the shape of the second object"""


        if point in self.shape1 and point not in self.shape2:
            return True
        else:
            return False


    def __repr__(self):
        """Creating a string representaion of the difference for the user as asked in the exercise"""


        return f"Difference of {self.shape1} from {self.shape2}."


def draw_pixel(canvas, x, y, color='blue'):
    """Draw a pixel at (x,y) on the given canvas"""
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def main(shape):
    """Create a main window with a canvas to draw on"""
    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    # Render the user-defined shape
    shape.draw(canvas)

    # Start the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)
    tk.mainloop()


if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    ##### IMPLEMENT ME ##########
    face = Circle(0, 0, 100)
    left_eye = Circle(-50, -50, 10)
    right_eye = Circle(50, -50, 10)
    mouth = Rectangle(-50, 80, 50, 20) & Circle(0, 20, 50) # Intersection of the rectangle and circle
    shape = face - (left_eye | right_eye | mouth) # Difference of the face from the union of left_eye, right_eye, and mouth objects
    main(shape)