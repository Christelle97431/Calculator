#!/usr/bin/env python3
from math import *

class Addition:
    total_add = ""

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def calcul_add(self):
        total_add = float(self.number1) + float(self.number2)
        print (f"resultat de la classe : {total_add}")
        return (total_add)
        
        

