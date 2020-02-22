#import pi for calculation
from math import pi

conversion_type = int(input("Which type of angle conversion do you need?\n(1) rad to degree\n(2) degree to rad\n"))
if conversion_type == 1:
    #convert angle from rad to degree
    def convert_angle_to_degree():
        angle_rad = float(input("Please enter the angle in rad "))
        angle_degree = (360 / (2 * pi)) * angle_rad
        print("The angle " + str(angle_rad) + " rad is equal to " + str(angle_degree) + " degrees")

    convert_angle_to_degree()
elif conversion_type == 2:
    #convert angle from degree to rad
    def convert_angle_from_degree():
        angle_degree = float(input("Please enter the angle in degree "))
        angle_rad = (angle_degree / 180) * pi
        print("The angle " + str(angle_degree) + " degree is equal to " + str(angle_rad) + " rad")

    convert_angle_from_degree()
else:
    print("Invalid input, please choose from one of the two conversion types.")