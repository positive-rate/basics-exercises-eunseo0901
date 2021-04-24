def single_operators():
    # Finish the sentences:
    print(f'Three plus seven is {3 + 7}')
    print(f'Five minus ten is ')
    print(f'Nine divided by three is ')
    print(f'Eight times seven is ')

def with_variables():
    # It's rare to just use numbers in programming. Normally the numbers are in
    # variables. Finish the sentences again:
    a = 12
    b = 4
    print(f'a plus b is {a + b}')
    print(f'a minus b is ')
    print(f'a divided b three is ')
    print(f'a times b is ')


def operator_combinations():
    # This exercise is not really about programming, but about math
    # You can combine + and - signs as much as you want, in math
    # Just apply from left to right:
    print(f'1 + 2 + 3 + 4 + 5 - 6 + 7 = {1 + 2 + 3 + 4 + 5 - 6 + 7}')

    # You can also combine * and / signs as much as you want,
    # and again apply them from left to right:
    print(f'3 * 4 / 6 * 2 = {3 * 4 / 6 * 2}')

    # But when you combine + or - with * or /, you have to be careful.
    # What is the answer here? Try to calculate it in your head first,
    # then write the code and check the answer:
    a = 2
    b = 3
    c = 4
    print(f'a + b * c = ')
    print(f'b * c + a = ')
    print(f'c * a + b = ')

    # What if you want to first add two numbers, and then multiply the result
    # by another number? Use parentheses:
    print(f'(a + b) * c = {(a + b) * c}')

    # You're getting a fourth number, d. Multiply a by b, and c by d, and then
    # add everything together and print the answer. Try to write it all in one
    # line.

def simple_series():
    # Please use a loop. Print all the numbers from 1 to 10.
    pass

def even_series():
    # Same as before, but print only the even numbers (2, 4, 6, ...)
    pass

def powers_of_two():
    # Please print the first 15 powers of two. That means: keep multiplying by 2.
    # The first number is 2, then 4, 8, 16, ...
    pass

def fibonacci():
    # This exercise is difficult. Try the simpler exercises in the other files first!

    # Print the first 20 numbers of the Fibonacci sequence. The rules for this sequence are:
    # The first number is 0.
    # The second number is 1.
    # Every later number is the sum of the two before it.
    #
    # So: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    pass

def main():
    print('Which exercise do you want to run?')
    print('1. Single operators')
    print('2. Single operators with variables')
    print('3. Operator combinations')
    print('4. Count to ten')
    print('5. Even numbers')
    print('6. Powers of two')
    print('7. Fibonacci')

    while True:
        try:
            exercise = int(input())
            if exercise < 1 or exercise > 7:
                print('Please enter a number from the list')
                continue
            if exercise == 1:
                single_operators()
            elif exercise == 2:
                with_variables()
            elif exercise == 3:
                operator_combinations()
            elif exercise == 4:
                simple_series()
            elif exercise == 5:
                even_series()
            elif exercise == 6:
                powers_of_two()
            elif exercise == 7:
                fibonacci()

            break
        except ValueError:
            print('Please enter a number')