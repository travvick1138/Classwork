#setup


#input
input_name = input("What is your name? ")

input_age = int(input("what is your age? "))


#transformation

age = (input_age+1)
name = input_name

#output
Hello_person = '''Hello, {name} you will be {age} on your next birthday, Yeah!! ''' .format(
        age=age,
        name=name
)


print(Hello_person)
