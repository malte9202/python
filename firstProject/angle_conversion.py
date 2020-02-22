#import pi for calculation
#catch type errors for invalid input

from math import pi

def angle_conversion(conversion_type, angle_to_convert):
    if conversion_type == 1:
        converted_angle = (360 / (2 * pi)) * angle_to_convert
        print(str(angle_to_convert) + " rad is equal to " + str(converted_angle) + " degree")
        return converted_angle
    else:
        converted_angle = (angle_to_convert / 180) * pi
        print(str(angle_to_convert) + " degree is equal to " + str(converted_angle) + " rad")
        return converted_angle


conversion_type = int(input("Which type of angle conversion do you need?\n(1) rad to degree\n(2) degree to rad\n"))
while conversion_type not in [1, 2]:
    conversion_type = int(input("Please enter 1 or 2 to choose the type of conversion." +
                                "Which type of angle conversion do you need?\n(1) rad to degree\n(2) degree to rad\n"))

angle_to_convert = float(input("Please enter the angle you want to convert "))

angle_conversion(conversion_type, angle_to_convert)
