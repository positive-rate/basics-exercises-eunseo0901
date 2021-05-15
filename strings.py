def simple_printing():
    # 1. Print a string with single quotes
    print('hello')

    # 2. Print a string with double quotes
    print("nice to meet you")

def variable_printing():
    # Store your name in this variable, then print a sentence with your name,
    # using that variable. Use the + operator to concatenate (glue together) strings.
    my_name = 'Eunseo'
    print('Hi my name is ' + my_name)

    # Use the my_name variable in another sentence, but this time use an f-string
    print(f"Hi my name is {my_name}")

def main():
    print('Which exercise do you want to run?')
    print('1. Simple printing')
    print('2. Printing with variables')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 2:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                simple_printing()
            elif exercise == 2:
                variable_printing()

            break
        except ValueError:
            print('Please enter a number')
