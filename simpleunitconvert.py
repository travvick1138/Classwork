#setup
feet_in_a_mile = 5280

#input

input_mile = int(input("How many miles? "))

#transformation

feet = (input_mile*feet_in_a_mile)


#output
print('{feet}' .format(
        feet=feet
))
