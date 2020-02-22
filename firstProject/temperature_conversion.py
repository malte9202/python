def convert_temperature():
    print(
        "(1) Convert Celsius to Kelvin\n(2) Convert Celsius to Fahrenheit\n(3) Convert Kelvin to Celsius\n" +
        "(4) Convert Kelvin to Fahrenheit\n(5) Convert Fahrenheit to Celsius\n(6) Convert Fahrenheit to Kelvin"
    )
    convert_type = int(input("Please enter the type of conversion: "))
    if convert_type in [1,2,3,4,5,6]:
        start_temp = float(input("Please enter the temperature to convert: "))
        if convert_type == 1:#Celsius to Kelvin
            new_temp = start_temp + 273.15
            print(str(start_temp) + " degree Celsius is equal to " + str(new_temp) + " degree Kelvin")
        elif convert_type == 2:#Celsius to Fahrenheit
            new_temp = (start_temp * 9 / 5) + 32
            print(str(start_temp) + " degree Celsius is equal to " + str(new_temp) + " degree Fahrenheit")
        elif convert_type == 3:#Kelvin to Celsius
            new_temp = start_temp - 273.15
            print(str(start_temp) + " degree Kelvin is equal to " + str(new_temp) + " degree Celsius")
        elif convert_type == 4:#Kelvin to Fahrenheit
            new_temp = (start_temp - 273.15) * 9 / 5 + 32
            print(str(start_temp) + " degree Kelvin is equal to " + str(new_temp) + " degree Fahrenheit")
        elif convert_type == 5:#Fahrenheit to Celsius
            new_temp = (start_temp - 32) * 5 / 9
            print(str(start_temp) + " degree Fahrenheit is equal to " + str(new_temp) + " degree Celsius")
        elif convert_type == 6:#Fahrenheit to Kelvin
            new_temp = (start_temp - 32) * 5 / 9 + 273.15
            print(str(start_temp) + " degree Fahrenheit is equal to " + str(new_temp) + " degree Kelvin")
    else:
        print("Invalid input, please choose a conversion type with numbers from 1 to 6")

convert_temperature()