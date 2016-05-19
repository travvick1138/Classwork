num_cents = int(input( "How much change? :"))

quarters_in_change = num_cents // 25
dime_in_change = num_cents % 25 // 10
nickels_in_change = num_cents % 25 // 10 // 5
pennies_in_change = num_cents % 25 // 10 // 5 // 1

print("You have" + str(quarters_in_change) + "quarters," + str(dime_in_change) + "dimes," + str(nickels_in_change) + "nickels, and"  + str(pennies_in_change) + "pennies.")
