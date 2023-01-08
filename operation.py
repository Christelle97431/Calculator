#!/usr/bin/env python3
from addition import Addition
from divide import Divide
from multiply import Multiply
from substract import Substract

class Operation:
     
     def __init__(self, ope, number1, number2):
          self.ope = ope
          self.number1 = number1
          self.number2 = number2
          
     def calcul(self):
          result=""
          if self.ope == "+":
               result=Addition.calcul_add(self)
               return(result)
          elif self.ope == "-":
               result = Substract.calcul_substract(self)
               return (result)
          elif self.ope == "*":
               result = Multiply.calcul_mulitply(self)
               return(result)
          elif self.ope == "/":
               result = Divide.calcul_divide(self)
               return(result)

          
          

# test=Operator('+', 2, 3)
# test.calcul()