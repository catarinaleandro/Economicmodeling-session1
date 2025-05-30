from color_point import ColorPoint

class AdvancedPoint(ColorPoint): #this means we are inheriting from color point
    COLORS = ["red", "green", "blue", "black", "white"]
    def __init__(self, x,y,color):
        """
        Magic method that initializes a more advanced point by validating coordinates and the color.
        :param x: x value (coordinate)
        :param y: y value (coordinate)
        :param color: color from list
        """
        if not isinstance(x, (int,float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of :{self.COLORS}")
        #super().__init__(x, y, color) #call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Method that defines the x coordinate as an attribute instead of a method
        :return: x value as an int/float
        """
        return self._x

    @property
    def y(self):
        """
        Method that defines the y coordinate as an attribute instead of a method
        :return: y value as an int/float
        """
        return self._y

    @property
    def color(self):
        """
        Defines the point's color as a str
        :return: current color of the point
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Defines a new color for the point while validating the color is in the list
        :param new_color: new color to assign
        :return: point with the new color
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of :{AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        """
        Adds a new color to the valid colors list
        :param new_color: new color to add
        :return: appended list
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculates the distance between two points
        :param p1: point 1
        :param p2: point 2
        :return: distance between the two
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)**0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Creates an advanced point from a dictionary
        :param dict: a dictionary containing x and y coordinates as well as colors
        :return: advanced point with the extracted values
        """
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)


AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1,2,"amber")
print(p2.x)
print(p2.y)
p2.color = "blue"
print(p2)
p3 = AdvancedPoint(-1,-2,"blue")
print(AdvancedPoint.distance_2_points(p2, p3))
p4 = AdvancedPoint.from_dictionary({})
print(p4)
