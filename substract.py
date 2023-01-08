#!/usr/bin/env python3

from math import *

class Substract:
    total_substract = ""

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def calcul_substract(self):
        total_substract = (float(self.number1) - float(self.number2))
        print (f"resultat de la classe substract : {total_substract}")
        return (total_substract)