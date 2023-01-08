# coding: utf-8

# couleurs : 
# noir : "#101419"
# rouge : "#DC2910"
# bleu : "#0460AE"

# Format de la calculatrice
# 4 colonnes à créer
#     789*
#     456-
#     123+
#     0./=

from tkinter import * 
from math import *

from operation import Operation
from addition import Addition

# variable stockant l'expression saisie sur la calculatrice
expressions = []


def appuyer(touche):

    if touche == "=":
        calculer()
        return
    
    global expressions
    # expression += (str(touche))
    expressions.append(str(touche))
    equation.set(expressions)
    print(f"expression saisie sur la calculatrice : {expressions}")


def calculer():
    get_ope=""
    number1=[]
    number2=[]
    index_op = ""

    global expressions
    # print(expressions)
    # total = str(eval(expression))
    # equation.set(total)
    # expression = total
    for elem in expressions:
        if elem in["+","-","*","/"]:
            get_ope=elem
            # print(f"opérateur : {get_ope}")
            index_op = expressions.index(get_ope)
            # print(f"index opérateur : {index_op}")

    # affiche les éléments avant la position de l"opérateur
    number1 = expressions[:index_op]
    # affiche les éléments après la position de l"opérateur
    number2 = expressions[(index_op+1):]
    # print(f"valeur number1: {number1}")
    # print(f"valeur number2: {number2}")
    number1 ="".join(number1)
    number2 ="".join(number2)
    # print(f"valeur number1: {number1}")
    # print(f"valeur number2: {number2}")
    print (number1, get_ope, number2,)
    # return (number1, get_ope, number2)

    test = Operation(get_ope, number1, number2)
    total = test.calcul()
    print(f"total {total}")
    equation.set(total)
    expressions = total
    print(f"expression : {expressions}")

    # print(expressions)
    # total = str(eval(expression))
    # equation.set(total)
    # expression = total


def effacer():
    global expressions
    expressions=[]
    # on efface le résultat de l'opération
    equation.set("")




# --------------------------------
# -- DESIGN DE LA CALCULATRICE ---
# --------------------------------

# code qui va créer le design de la calculatrice
window = Tk()

# couleur de fond
window.configure(background="#101419")

# titre de l'application
window.title("calculatrice")

# taille  de l'application
window.geometry("185x560")

# variable pour stocker le contenu actuel
equation = StringVar()

# boite d'affichage du résultat
resultat = Label(window, bg="#101419", fg="#fff", textvariable=equation, height="4")
resultat.grid(columnspan=4)

# boite d'affichage du clavier
boutons = ["HYP","SIN","COS","TAN","π","1/x","x2","√x","∑+","^","(",")",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,".","/","="]
ligne = 1
colonne = 0

for bouton in boutons:
    b = Label(window, text=str(bouton), bg="#0460AE", fg="#fff", borderwidth=1, relief=RAISED, height=4, width=6)
    # rendre le texte cliquable avec la fonction lambda
    # lambda mot clé, variable/argument lié:expression
    # le paramètre est ici le chiffre/symbole du bouton
    b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))
    # le bouton s'affichera dans la ligne et la colonne donnée
    b.grid(row=ligne, column=colonne)

    colonne += 1
    # si les 4 colonnes sont complétées, on incrémente la ligne de 1 pour écrire sur une autre ligne et la colonne repasse à 0
    if colonne == 4:
        colonne = 0
        ligne += 1

# bouton pour effacer
b = Label(window, text="Clear", bg="#DC2910", fg="#fff", height=3, width=26)
b.bind("<Button-1>",lambda e: effacer())
b.grid(columnspan=4)

# ouverture de la calculatrice
window.mainloop()






