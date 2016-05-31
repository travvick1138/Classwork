from random import randint

def dices(number_of_dice, number_of_sides):
    for  die in range(1, number_of_dice + 1):
        print("Die number " + str(die) + ": " + str(randint(1, number_of_sides)))

dice_number = int(input("How many dice you like to roll?"))
dice_sides = int(input("How many sides should each die have?"))

dices(dice_number, dice_sides)
