#!/usr/bin/python3.4
# -*-coding:Utf-8 -*


def check():
    annee = int(input("Saisissez une annee : "))

    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                print(annee, "est une annee bissextile")
            else:
                print(annee, "n'est pas une annee bissextile")
        else:
            print(annee, "est une annee bissextile")
    else:
        print(annee, "n'est pas une annee bissextile")

if __name__ == "__main__":
    check()
