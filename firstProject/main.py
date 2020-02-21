#Aufgabe 1: Textausgabe
#print("Name: Malte Niedereichholz")

#Aufgabe 2: Umrechnung von Winkeln
#from math import pi
#def winkel_umrechnung_rad_in_grad():
#    winkel_bogenmass = float(input("Geben Sie den Winkel im Bogenmaß ein: "))
#    winkel_grad = (360/(2*pi))*winkel_bogenmass
#    print("Das Bogenmaß " + str(winkel_bogenmass) + " rad entspricht dem Gradmaß " + str(round(winkel_grad)) + "°")

#winkel_umrechnung_rad_in_grad()

#def winkel_umrechnung_grad_in_rad():
#    winkel_grad = float(input("Geben Sie den Winkel in Grad ein: "))
#    winkel_bogenmass = (winkel_grad/180)*pi
#    print("Das Gradmaß " + str(winkel_grad) + "° entspricht dem Bogenmaß " + str(winkel_bogenmass) + " rad")

#winkel_umrechnung_grad_in_rad()

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
