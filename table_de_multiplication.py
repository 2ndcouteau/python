#!/usr/bin/python3.4
# -*-coding:Utf-8 *-

while 1:
    table = input("Saisissez la table a afficher ou 'Q' pour quitter: ")
    if table == 'Q':
        print("A bientot")
        break
    try:
        table = int(table)
        maxi = input("Saisissez le maximum a calculer ou 'Q' pour quitter: ")
        if maxi == 'Q':
            print("A bientot")
            break
        try:
            maxi = int(maxi)
            nb = 0
            print("\n##################")
            while nb < (maxi + 1):  #Cacul of table
                print(nb, "*", table, "=", nb * table)
                nb += 1
            print("##################\n")
        except ValueError:
            print("\n--", maxi, "--", "n'est pas valide.","\nMerci de saisir un maximum valide.\n")

    except ValueError:
        print("\n--", table, "--", "n'est pas valide.","\nMerci de saisir une table valide.\n")
