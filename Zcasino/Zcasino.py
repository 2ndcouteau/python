#!/usr/bin/python3.4
# -*- coding:Utf-8 -*

from math import ceil
from random import randrange
from sys import exit
from time import sleep

def quitter():
    print("\nSee you soon -- Kiss")
    exit(0)


def presentation():
    choice = 0
    while choice < 1 or choice > 3:
        print("\nHello and Welcome in the MegaMaxiRoulette Casino of Bonpigeon.\n\nPlease Choose the value of your Hand:\n 1) Rich AssHole 1000$\n 2) Fucked Worker 200$\n 3) Poor Son of a Bitch 10$ \n\nFor Win you need to win 2000$ -- Good Luck!\n\n(Yeah, i know for the Rich it's fucking easy but it is the life <3)")
        choice = input("\n----------------------\n\nPlease choose one difficulty. Write 1, 2 or 3 and press Enter, or 'Q' for quit the game\n\nPlease enter you choice here : ")
        if choice == 'Q':
            quitter()
        try :
            choice = int(choice)
            if choice < 1 or choice > 3:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$ Bad choice, please Try Again ! $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n----------------------\n")
        except ValueError:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$ Bad character(s), please Try Again ! $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n----------------------\n")
            choice = 0

    if choice == 1:
        print("Welcome My Lord.\n")
        value = 1000
    elif choice == 2:
        print("May the force be with you.\n")
        value = 200
    else:
        print("God said : We have to share, the Rich will have food, Poor hungry.\n")
        value = 10
    return value

def howmany_bet(value):
    # Check How many bet.
    valid = False
    print("     \"Place your bets\"\n")
    while valid is False:
        print("Your have", value,"$")
        print("How many will you bet ?")
        mise = input("Write here your bet : ")
        if mise == 'Q':
            quitter()
        try:
            mise = int(mise)
            if mise > value:
                print("The house does not offer credit FDP !\n")
            elif mise <= 0:
                print("Don't be an idiot, I don't pick money in tree\n")
            else:
                valid = True
        except ValueError:
            print("Enter a number please.\n")
        print()
    return(mise)

def number_bet():
    # Check on which number bet.
    valid = False
    print("Which number do you want to choice ?\nEven is Black and Odd is Red")
    while valid is False:
        number = input("Write number between 0 and 49 : ")
        if number == 'Q':
            quitter()
        try:
            number = int(number)
            if number >= 0 and number <= 49:
                valid = True
        except ValueError:
            print("Enter a number please.\n")
        print()
    return(number)

def check_color(number_g):
    if(number_g % 2) == 0:
        color = "Black"
    else:
        color = "Red"
    return color

def round(mise_g, number_g, value):
    color = check_color(number_g)
    print("You bet", mise_g, "$ on the $$", number_g, color, "$$")
    rdm = randrange(50)
    print("\n     \"No more bets\"\n")
    color_rdm = check_color(rdm)
    sleep(2)
    print("The ball rolls.\n")
    sleep(1)
    print("...\n")
    print("Even few seconds...\n")
    sleep(2)
    print("     \"And the number is the $$", rdm, color_rdm, "$$\"")
    sleep(1)
    if number_g == rdm:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$      Congratulations, You win", mise_g * 3, "$.      $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
        value += mise_g * 3
    elif number_g % 2 == rdm % 2:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$      Cool! You choosed the good color, you win", mise_g / 2,"$.      $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
        value += ceil(mise_g / 2)
    else:
        print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n$      \"LOL you loose", mise_g,"$, EZLIFE.      $\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
        value -= mise_g
    return (value)

def game(value):
    while value < 2000 and value > 0:  # Define Value of Victory -- Don't forget to change it for the end message.
        mise_g = howmany_bet(value)
        number_g = number_bet()
        value = round(mise_g, number_g, value)
    if value > 2000:
        print("<3 <3 <3 --Oh my GOD ! You did it !-- <3 <3 <3\nPlease come back soon for try to win more $$$ -- KISS.\n")
    else:
        print("You are a fucking Asshole, just poor person... You merits that we spit on you!\nCome back soon for spend your poverty!\n")

if __name__ == "__main__":
    value = presentation()
    game(value)
