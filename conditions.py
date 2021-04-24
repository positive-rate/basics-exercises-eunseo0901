def simple_conditions():
    a = 7
    b = 12
    c = 12
    d = 2

    # Complete all the statements
    print(f'a is larger than b: {a > b}')
    print(f'b is smaller than c: ')
    print(f'b is larger than or equal to c: ')
    print(f'c is smaller than or equal to b: ')
    print(f'b is equal to c: ')
    print(f'a is not equal to d: ')

def composite_conditions():
    a = 1
    b = 2
    c = 4
    d = 8

    # Complete all statements
    print(f'c is twice as big as a: {c == 2 * a}')
    print(f'd is four times as big as b: ')
    print(f'c is a plus b: ')
    print(f'd divided by c is b: ')

def combining_conditions():
    a = True
    b = False
    c = 3 > 4

    # Complete all statements
    print(f'a is true and c is false: {a and not c}')
    print(f'a is true or b is true: ')
    print(f'c is false and b is false: ')
    print(f'c is true or 2 + 2 is 4: ')

def if_else():
    # Use code to check if the length of the story is more than 100.
    # If it is more than 100, print "That is a long story!"
    # Else, print "Not such a long story"
    # Hint: use len(story) to get the length of story
    story = 'Fiji is a small country in the Pacific Ocean. It has 322 islands. The most important islands are Vanua Levu and Viti Levu.'

def else_if():
    # Did you know you can use 'elif' as a short form of 'else if'?
    # You use it when you want to check multiple things.
    # You can see an example at the bottom of this file.
    # Give it a try yourself. Let's check some things.
    # Ask the user for a number below 10:
    number = int(input('Please give me a number between 1 and 10: '))

    # If the number is lower than 3, print "You like small numbers"
    # Else, if the number is lower than 7, print "7 would be a better choice"
    # Else, if the number is 7, print "I knew you would choose 7"
    # Else, print "You like big numbers"

def main():
    print('Which exercise do you want to run?')
    print('1. Simple conditions')
    print('2. Calculated conditions')
    print('3. Combining conditions')
    print('4. if else')
    print('5. elif')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 5:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                simple_conditions()
            elif exercise == 2:
                composite_conditions()
            elif exercise == 3:
                combining_conditions()
            elif exercise == 4:
                if_else()
            elif exercise == 5:
                else_if()

            break
        except ValueError:
            print('Please enter a number')
