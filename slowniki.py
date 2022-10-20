import os

slownik = {}

zdanie = "lubie jesc lody i lubie tooooo"

for z in zdanie:
    if z == " ":
        pass
    else:
        if z in slownik:
            slownik[z] += 1
        else:
            slownik[z] = 1

print(slownik)

liczba = 10.0322112321312321
from math import pi
print("%.10f" %pi)
