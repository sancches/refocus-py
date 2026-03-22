#tool to convert diferent units


#clear console function
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#conversion dictionary
#length - using meter as base
TO_METERS = {
    "km": {"name":"Kilometer" ,"factor":1000},
    "mi": {"name":"Mile" ,"factor":1609.34},
    "m": {"name":"Meter" ,"factor":1},
    "ft": {"name":"Feet" ,"factor":0.3048},
    "in": {"name":"Inch" ,"factor":0.0254},
    "cm": {"name":"Centimeter" ,"factor":0.01},
    "mm": {"name":"Milimeter" ,"factor":0.001}
}
#weight - using gram as base
TO_GRAMS = {
    "t": {"name":"Metric ton" ,"factor":1000000},
    "kg": {"name":"Kilogram" ,"factor":1000},
    "lb": {"name":"Pound" ,"factor":453.59},
    "oz": {"name":"Ounce" ,"factor":28.34},
    "g": {"name":"Gram" ,"factor":1},
    "ct": {"name":"Carat" ,"factor":0.2},
    "mg": {"name":"Miligram" ,"factor":0.001}
}
#volume - using liter as base
TO_LITERS = {
    "osp": {"name":"Olympic Swimming Pool" ,"factor":2500000},
    "m3": {"name":"Cubic Meter" ,"factor":1000},
    "bbl": {"name":"Barrel" ,"factor":159},
    "ft3": {"name":"Cubic foot" ,"factor":28.31},
    "l": {"name":"Liter" ,"factor":1},
    "gal": {"name":"Gallon" ,"factor":4.54},
    "ml": {"name":"Mililiter" ,"factor":0.001}
    
    
}

#temperature
#since temperature conversion isn't linear, we can't do the same as the others
def to_celsius(value, unit):
    if unit == "c":
        return value
    elif unit == "f":
        return (value - 32) * 5/9
    elif unit == "k":
        return value - 273.15

def from_celsius(value, unit):
    if unit == "c":
        return value
    elif unit == "f":
        return (value * 9/5) + 32
    elif unit == "k":
        return value + 273.15

#temperature-only conversion operation
def convert_temperature(value, from_unit, to_unit):
    return from_celsius(to_celsius(value, from_unit), to_unit)

#general conversion operation
def convert(value, from_unit, to_unit, conversion_table):
    base = value * conversion_table[from_unit]["factor"]
    return base / conversion_table[to_unit]["factor"]

def menu():
    while True:
        try:
            print("Unit converter 1.0 \n")
            print("1.  Length")
            print("2.  Weight")
            print("3.  Volume")
            print("4.  Temperature")
            print("0.  Exit program \n")
            type = int(input("choose your type(1-4): "))
            clear()


            #options (1-4)
            if type==1:
                while True:
                    print("Length selected, valid units:\n")

                    for abbrev, info in TO_METERS.items():
                        print(f"({abbrev}).  {info['name']}")

                    try:
                        value = float(input("\nEnter the initial numeric value: "))
                        from_unit = str(input("Enter the initial unit (Ex: km): "))
                        if from_unit not in TO_METERS:
                            raise ValueError
                        to_unit = str(input("Enter the desired unit to be converted (Ex: cm): "))
                        if to_unit not in TO_METERS:
                            raise ValueError

                        clear()
                        print(f"Converting ({value} {from_unit}) into ({to_unit}) result: ", round(convert(value, from_unit, to_unit, TO_METERS),2), to_unit)
                        break

                    except ValueError:
                        clear()
                        print("Error: Input type is incorrect")

            elif type==2:
                while True:
                    print("Weight selected, valid units:\n")

                    for abbrev, info in TO_GRAMS.items():
                        print(f"({abbrev}).  {info['name']}")

                    try:
                        value = float(input("\nEnter the initial numeric value: "))
                        from_unit = str(input("Enter the initial unit (Ex: kg): "))
                        if from_unit not in TO_GRAMS:
                            raise ValueError
                        to_unit = str(input("Enter the desired unit to be converted (Ex: lb): "))
                        if to_unit not in TO_GRAMS:
                            raise ValueError

                        clear()
                        print(f"Converting ({value} {from_unit}) into ({to_unit}) result: ", round(convert(value, from_unit, to_unit, TO_GRAMS),2), to_unit)
                        break

                    except ValueError:
                        clear()
                        print("Error: Input type is incorrect")


            elif type==3:
                while True:
                    print("Volume selected, valid units:\n")

                    for abbrev, info in TO_LITERS.items():
                        print(f"({abbrev}).  {info['name']}")

                    try:
                        value = float(input("\nEnter the initial numeric value: "))
                        from_unit = str(input("Enter the initial unit (Ex: l): "))
                        if from_unit not in TO_LITERS:
                            raise ValueError
                        to_unit = str(input("Enter the desired unit to be converted (Ex: m3): "))
                        if to_unit not in TO_LITERS:
                            raise ValueError

                        clear()
                        print(f"Converting ({value} {from_unit}) into ({to_unit}) result: ", round(convert(value, from_unit, to_unit, TO_LITERS),2), to_unit)
                        break

                    except ValueError:
                        clear()
                        print("Error: Input type is incorrect")

            elif type==4:
                while True:
                    print("Temperature selected, valid units:\n")

                    print("(c).  Celsius")
                    print("(f).  Fahrenheit")
                    print("(k).  Kelvin")   
                    VALID_TEMPS = ["c", "f", "k"] # redneck way to atone for not having a dictionary for temperature factors
                    try:
                        value = float(input("\nEnter the initial numeric value: "))
                        from_unit = str(input("Enter the initial unit (Ex: c): "))
                        if from_unit not in VALID_TEMPS:
                            raise ValueError
                        to_unit = str(input("Enter the desired unit to be converted (Ex: f): "))
                        if to_unit not in VALID_TEMPS:
                            raise ValueError

                        clear()
                        print(f"Converting ({value} {from_unit}) into ({to_unit}) result: ", round(convert_temperature(value, from_unit, to_unit),2),to_unit)
                        break

                    except ValueError:
                        clear()
                        print("Error: Input type is incorrect")
                
            elif type==0:
                clear()
                print("Leaving program")
                break


            else:
                clear()
                print("Error: Input is not a valid option")


        #handles other response
        except ValueError:
            clear()
            print("Error: Input type is incorrect")


menu()