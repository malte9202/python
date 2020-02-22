#Aufgabe 1: print text
print("Name: Malte Niedereichholz")

#Aufgabe 2: angle conversion
from math import pi
def convert_angle_to_degree():
    angle_rad = float(input("Please enter the angle in rad "))
    angle_degree = (360 / (2 * pi)) * angle_rad
    print("The angle " + str(angle_rad) + " rad is equal to " + str(angle_degree) + " degrees")

convert_angle_to_degree()

def convert_angle_from_degree():
    angle_degree = float(input("Please enter the angle in degree "))
    angle_rad = (angle_degree / 180) * pi
    print("The angle " + str(angle_degree) + "degree is equal to " + str(angle_rad) + " rad")

convert_angle_from_degree()

#Aufgabe 3: Umrechnung von Temperaturen
def temperatur_umrechnung():
    print(
        "(1) Umrechnung von Celsius nach Kelvin\n(2) Umrechnung von Celsius nach Fahrenheit\n(3) Umrechnung von Kelvin nach Celsius\n" +
        "(4) Umrechnung von Kelvin nach Fahrenheit\n(5) Umrechnung von Fahrenheit nach Celsius\n(6) Umrechnung von Fahrenheit nach Kelvin"
    )
    umrechnungs_typ = int(input("Bitte wählen Sie aus, welche Umrechnung vorgenommen werden soll: "))
    start_temp = float(input("Bitte geben Sie die umzurechnende Temperatur ein: "))
    if umrechnungs_typ == 1:
        new_temp = start_temp + 273.15
        print(new_temp)
    elif umrechnungs_typ == 2:
        new_temp = (start_temp * 9 / 5) + 32
        print(new_temp)
    elif umrechnungs_typ == 3:
        new_temp = start_temp - 273.15
        print(new_temp)
    elif umrechnungs_typ == 4:
        new_temp = (start_temp - 273.15) * 9 / 5 + 32
        print(new_temp)
    elif umrechnungs_typ == 5:
        new_temp = (start_temp - 32) * 5 / 9
        print(new_temp)
    elif umrechnungs_typ == 6:
        new_temp = (start_temp - 32) * 5 / 9 + 273.15
        print(new_temp)
    else:
        print("Ungültige Eingabe")

temperatur_umrechnung()
