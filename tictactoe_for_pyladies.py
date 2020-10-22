from random import randrange

def vyhodnot(hraci_pole):
    if "xxx" in hraci_pole:
        print(hraci_pole)
        print("Vyhrál x!")
        return 1
    elif "ooo" in hraci_pole:
        print(hraci_pole)
        print("Vyhrál o!")
        return 1
    elif "-" not in hraci_pole:
        print(hraci_pole)
        print("Plichta!")
        return 1
    else:
        print("-")

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    pole = list(pole)
    pole[cislo_policka] = symbol
    pole = "".join(pole)
    return pole

def tah_hrace(pole_hrace, symbol):
    print(pole_hrace)
    while True:
        cislo_policka = int(input("Kam chceš hrát - zvol číslo 0-19? "))
        if cislo_policka in range(0, 20) and list(pole_hrace)[cislo_policka] == "-":
            pole_hrace = list(pole_hrace)
            pole_hrace[cislo_policka] = symbol
            pole_hrace = "".join(pole_hrace)
            return pole_hrace
        elif cislo_policka not in range(20):
            print("Přečti si znovu zadání!")
        else:
            print("Tam je plno!")

def tah_pocitace(pole_pocitace, symbol_pocitace):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        cislo_policka = randrange(20)
        if list(pole_pocitace)[cislo_policka] == "-":
            pole_pocitace = list(pole_pocitace)
            pole_pocitace[cislo_policka] = symbol_pocitace
            pole_pocitace = "".join(pole_pocitace)
            return pole_pocitace


def piskvorky1d():
    pole = "-" * 20
    symbol = input("Jaký chceš symbol? (x/o):")
    symbol_pocitace = "x"
    if symbol == "x":
        symbol_pocitace = "o"

    while vyhodnot(pole) != 1:
        pole = tah_hrace(pole, symbol)
        if vyhodnot(pole) == 1:
            break
        pole = tah_pocitace(pole, symbol_pocitace)

piskvorky1d()