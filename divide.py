#!/usr/bin/env python3

from math import *

class Divide:
    total_divide = ""

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def calcul_divide(self):
        if float(self.number2) == 0:
            # raise Exception("You can not divide by 0 !")
            return("#DIV/0! error")
        else:
            total_divide = (float(self.number1) / float(self.number2))
            print (f"resultat de la classe divide : {total_divide}")
            return (total_divide)