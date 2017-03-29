#!/usr/bin/python3.4
# -*- coding:Utf8 -*

def affiche_flottant(number):
    entiere, decimal = number.split(".")
    lst = (entiere, decimal[0:3])
    rep = ",".join(lst)
    print(rep)

if __name__ == "__main__":
    number = str()
    while 1:
        try:
            number = input("Entrez un nombre flottant ou 'Q' pour quitter: ")
            if number.lower() == 'q' :
                print("\nGood Bye\n")
                break
            float(number)
            affiche_flottant(number)
        except ValueError:
            print("Erreur, veuillez entrer un nombre flottant\n")

