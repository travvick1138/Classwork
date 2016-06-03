#setup
feet_in_a_mile = 5280

#input

input_mile = float(input("How many miles? "))

#transformation

miles = input_mile
feet = (input_mile*feet_in_a_mile)


#output
how_many_feet = '''This is how many feet {feet} in this many miles {miles}.''' .format(
        feet=feet,
        miles=miles
)
print(how_many_feet)
