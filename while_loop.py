def simple_print():
    # print the number 7
    pass

def many_print():
    # print the number 7 seven times (each on a new line)
    pass

def long_print():
    # print '7777777' (seven 7s)
    # hint: you can print 'aaa' by saying print('a' * 3)
    pass

def increasing_print():
    # print '1' and then '22' and then '333', etc. up to '7777777'. 
    pass

def increasing_print_input():
    # ask the user for a number between 0 and 10
    # if the user gives a wrong number, or not a number, print an error
    # otherwise, print '1' and then '22', then '333', etc. up to the number the user said
    pass

def main():
    print('Which exercise do you want to run?')
    print('1. Seven')
    print('2. Seven sevens')
    print('3. String of sevens')
    print('4. Increasingly long strings of numbers')
    print('5. User input strings of numbers')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 5:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                simple_print()
            elif exercise == 2:
                many_print()
            elif exercise == 3:
                long_print()
            elif exercise == 4:
                increasing_print()
            elif exercise == 5:
                increasing_print_input()

            break
        except ValueError:
            print('Please enter a number')
