#!/usr/bin/python3.4
# _*_ coding:Utf-8 -*

def affichage(pimp, signature, *params, ponctuation="..", sep=' ', end='\n'):
    tmp = sep.join(params)
    lst = [pimp, tmp, signature, pimp + end]
    chaine = " ".join(lst)
    print(chaine)

if __name__ == "__main__":
    signature = "EZLIFE"
    pimp = "$$$"
    phrase = input("Entrez le texte a Afficher : ")
    phrase2 = input("Entrez la suite du texte a Afficher : ")
    affichage(pimp, signature, phrase, phrase2, ponctuation="!!!")
