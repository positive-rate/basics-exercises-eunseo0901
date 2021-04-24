def string_input():
    # Use print() a message asking the user to enter their name
    # Get the user their name using input()
    # Print a message with the user their name
    pass

def question_input():
    # Ask the user a question using the input() function, and store the answer
    # Print a sentence using the answer
    # What is the difference between using print() and input() to ask the question?
    pass

def int_input():
    # Ask the user for a number, and store it in a variable
    # Convert the number to an int
    # Print the answer to 42 times the number
    pass

def main():
    print('Which exercise do you want to run?')
    print('1. String input')
    print('2. Using input to ask a question')
    print('3. Converting input to int')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 3:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                string_input()
            elif exercise == 2:
                question_input()
            elif exercise == 3:
                int_input()

            break
        except ValueError:
            print('Please enter a number')
