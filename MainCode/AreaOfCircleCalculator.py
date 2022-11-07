import math


class CircleAreaCalculator:

    def __init__(self):
        self.radius = None

    def __get_input(self):
        try:
            radius = float(input("Please enter the radius of the circle in cm: "))
            self.radius = radius
        except ValueError:
            print("Invalid value for the radius passed, Please enter a number as the radius")
            self.__get_input()
            return

    def __calculate_circle_area(self):
        # Pi * r^2
        result = math.pi * math.pow(self.radius, 2)
        print(f"The area of the circle of radius {self.radius} cm is: {result} cm-squared")

    def run(self):
        print("Hello there, welcome to my Circle Area Calculator App.\n"
              "Please enter the required data below\n"
              "------------------------------------------------------------\n")
        self.__get_input()
        self.__calculate_circle_area()
