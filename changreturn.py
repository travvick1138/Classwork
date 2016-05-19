# setup
Quarters = 25
Dimes = 10
Nickels = 5
Cents = 1

# input
input_cents = int(input("How many cents do you have? "))

# transformation
number_of_quarters = input_cents // Quarters
number_of_dimes = (input_cents - (Quarters*number_of_quarters)) // Dimes
number_of_nickels = (input_cents - ((Quarters*number_of_quarters)+(Dimes*number_of_dimes))) // Nickels
number_of_cents = (input_cents - ((Quarters*number_of_quarters)+(Dimes*number_of_dimes)+(Nickels*number_of_nickels))) // Cents

# output
Your_change = '''                 Quarters = {Quarters}
                 Dimes    = {Dimes}
                 Nickels  = {Nickels}
                 Cents    = {Cents}'''.format(

    Cents=number_of_cents,
    Nickels=number_of_nickels,
    Dimes=number_of_dimes,
    Quarters=number_of_quarters
)

print(Your_change)
