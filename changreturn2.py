
input_cents = int(input("How many cents do you have? "))



number_of_quarters = input_cents // 25
number_of_dimes = input_cents % 25 // 10
number_of_nickels = input_cents % 25 // 10 // 5
number_of_cents = input_cents % 25 // 10 // 5 // 1



print("Your change " + str(number_of_quarters) + " quarters," + str(number_of_dimes) + " dimes," + str(number_of_nickels) + " nickels," + str(number_of_cents) + " cents.")
