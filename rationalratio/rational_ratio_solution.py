import sys
from math import gcd

def find_fraction():
    f = sys.stdin
    contents =f.read()
    number_str = contents.split()[0]
    number = float(number_str)
    repeating = int(contents.split()[-1])
    
    number_list = number_str.split(".")
    decimal_places = len(number_list[1])
    number_nodecimal = int(number_list[0]+number_list[1])
    number_nonrepeating = int(number_list[0]+number_list[1][0:-repeating])

    numerator = number_nodecimal - number_nonrepeating
    denominator = 0

    for i in range(decimal_places, decimal_places-repeating, -1):
        denominator += 9*(10**(i-1))

    gcd_ = gcd(numerator, denominator)
    numerator = numerator // gcd_
    denominator = denominator // gcd_

    print(str(numerator) + "/" + str(denominator))

   # print("%0.15f"%eulers_number)

find_fraction()