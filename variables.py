def use_variables():
    # You have two variables here, both are numbers:
    days_in_week = 7
    hours_in_day = 24

    # Make a new variable to store the amount of hours in a week
    # and assign it the correct value (multiply using '*')

def reassignment():
    # Read this code, and write behind each line what the values of the variables are.
    a = 7 # a = 7
    b = 3 # a = 7, b = 3
    c = a # a = 7, b = 3, c = 7
    a = 4
    c = c + 1
    b += 2
    a = "Busan"

def main():
    print('Which exercise do you want to run?')
    print('1. Using variables')
    print('2. Assigning values to variables')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 2:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                use_variables()
            elif exercise == 2:
                reassignment()

            break
        except ValueError:
            print('Please enter a number')
