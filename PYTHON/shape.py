class Circle:
    pi = 3.14159
    def __init__(self,radius,color="black",filled=False):
        self.r = radius
        self.__c = color
        self.fill = filled

    def area(self):
        return "Area of Circle: {}".format(self.pi*self.r * self.r)

    def filled(self):
        return "Filled: {}".format(self.fill)

    def diameter(self):
        return "Diameter: {}".format(self.r*2)

    def getColor(self):
        return "Color: {}".format(self.__c)

    def setColor(self,color):
        self.__c = color
        print("Color set to ",self.__c)

    def __repr__(self):
        return "Radius for object is {}".format(self.r)

    def __eq__(self,otherCircle):
        return self.r == otherCircle.r and self.__c == otherCircle.__c

    def __lt__(self,otherCircle):
        if(self.r < otherCircle.r):
            return "Circle with radius {} is Larger".format(otherCircle.r)
        else:
            return "Circle with radius {} is larger".format(self.r)
