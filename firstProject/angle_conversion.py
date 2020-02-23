#import pi for calculation
from math import pi

#function to convert angles from rad to degree and from degree to rad
def angle_conversion(conversion_type, angle_to_convert):
    if conversion_type == 1:
        converted_angle = round((360 / (2 * pi)) * angle_to_convert,2)
        print(str(angle_to_convert) + " rad is equal to " + str(converted_angle) + " degree")
        return converted_angle
    else:
        converted_angle = round((angle_to_convert / 180) * pi,2)
        print(str(angle_to_convert) + " degree is equal to " + str(converted_angle) + " rad")
        return converted_angle

def get_conversion_type():
    conversion_type = None
    while conversion_type not in [1, 2]:
        try:
            conversion_type = int(input("Enter 1 or 2 to choose the type of conversion." +
                                        "Which type of angle conversion do you need?\n(1) rad to degree\n(2) degree to rad\n"))
        except ValueError:
            print("Please enter 1 or 2 to choose the type of conversion.")
    return conversion_type

def get_angle_to_convert():
    angle_to_convert = None
    while isinstance(angle_to_convert, float) == False:
        try:
            angle_to_convert = float(input("Enter the angle you want to convert "))
        except ValueError:
            print("The angle has to be a numeral\nPlease enter a valid value")
    return angle_to_convert

angle_conversion(get_conversion_type(), get_angle_to_convert())
