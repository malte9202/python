#Aufgabe 1
print("Name: Malte Niedereichholz\nGeburtsdatum: 20.02.1992\nAnschrift: Siedlungsstr. 12, 59069 Hamm")

#Aufgabe 2
from math import pi
def winkel_umrechnung_rad_in_grad():
    winkel_bogenmass = float(input("Geben Sie den Winkel im Bogenmaß ein: "))
    winkel_grad = (360/(2*pi))*winkel_bogenmass
    print("Das Bogenmaß " + str(winkel_bogenmass) + " rad entspricht dem Gradmaß " + str(round(winkel_grad)) + "°")

winkel_umrechnung_rad_in_grad()

def winkel_umrechnung_grad_in_rad():
    winkel_grad = float(input("Geben Sie den Winkel in Grad ein: "))
    winkel_bogenmass = (winkel_grad/180)*pi
    print("Das Gradmaß " + str(winkel_grad) + "° entspricht dem Bogenmaß " + str(winkel_bogenmass) + " rad")

winkel_umrechnung_grad_in_rad()

