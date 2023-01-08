#!/usr/bin/env python3
from math import *

class Multiply:
    total_multiply = ""

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def calcul_mulitply(self):
        total_multiply = (float(self.number1) * float(self.number2))
        print (f"resultat de la classe multiply : {total_multiply}")
        return (total_multiply)