input_one = input('Give me a number')

input_two = input('Give me a pural noun')

input_three = input('Give me a noun')

input_four = input('Give me an adjective')

input_five = input('Give me a number')

input_six = input('Give me a number')

input_seven = input('Give me a noun')

input_eight = input('Give me a noun')

input_nine = input('Give me a noun')

input_ten = input('Give me a noun')

input_eleven = input('Give me an adjective')

input_twelve = input('Give me an adjective')


My_story = '''This workbook is composed of {number_1} worksheets where {Pural_Noun} must insert a certain type of {noun_1} in a short paragraph to create a {adjective_1} story. Each worksheet is on a different topic related to summer. There are {number_2} sheets that require {Pural_Noun} to enter {number_3} {noun_2}, 10 {noun_3} that require students to enter eight words, and 10 {noun_4} that require {Pural_Noun} to enter ten {noun_5}. These are {adjective_2} practice for learning parts of speech and {adjective_3} for all elementary levels.
'''

My_transformed_story = My_story.format(
        number_1=input_one,
        Pural_Noun=input_two,
        noun_1=input_three,
        adjective_1=input_four,
        number_2=input_five,
        number_3=input_six,
        noun_2=input_seven,
        noun_3=input_eight,
        noun_4=input_nine,
        noun_5=input_ten,
        adjective_2=input_eleven,
        adjective_3=input_twelve
)

print(My_transformed_story)
