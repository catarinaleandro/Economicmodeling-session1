import random
from itertools import count


class Point:
    """
    Class modeling a real life 20 point
    """
    def __init__(self, x, y):
        """
        Initialize the point instance
        :param x: the x axis coordinate value
        :param y: the y axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Magic method that defines how a point is printed
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Magic method that defines the string representation of a point.
        :return: the point as a string
        """
        return self.__str__()

    def distance_orig(self):
        """
        Finds the distance from the point to the origin
        :return: distance number
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Magic method that is called when you do self>other
        :param other: the other point comparing against
        :return: True/False
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        """
        Magic method that defines if a point is equal to another based on the distance to origin
        :param other: different point
        :return: returns function True or False
        """
        return self.distance_orig() == other.distance_orig()


p1 = Point(1,2) #create a new instance
p2 = Point(3,4)
p3 = Point("James", "Jane") #this is valid, but prob not intended

#print(p1.x,p1.y) #access attributes
#print(p1)

if __name__ == "__main__":
    points = []
    for i in range(5):
        #create a random point
        p = Point(
            random.randint(-100,100),
            random.randint(-100, 100)
        )
        #append it to the list
        points.append(p)

    for point in points:
        print(point)

    print(points) #repr prints out the list
    #points.sort()
    p = Point(-12,-5)
    print(p.distance_orig())

    print("unsorted points")
    print(points)
    print("sorted points")
    points.sort()
    print(points)

    found_equal = 0
    count = 0
    while True:
        if found_equal == 10:
            break
        p1 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        p2 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        count+= 1
        if p1 == p2:
            print(p1, p2)
            found_equal += 1

    print(f"probability is 1 in {count/found_equal} ")