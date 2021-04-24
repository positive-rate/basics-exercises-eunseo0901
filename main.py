import basic_math
import basic_input
import conditions
import lists
import strings
import variables
import while_loop

def main():
    print('From which group do you want to run an exercise?')
    print('1. Strings')
    print('2. Input')
    print('3. Variables')
    print('4. Condditions')
    print('5. Math')
    print('6. While loops')

    while True:
        try:
            group = int(input())
            if group < 1 or group > 6:
                print('Please enter a number from the list')
                continue
            if group == 1:
                strings.main()
            elif group == 2:
                basic_input.main()
            elif group == 3:
                variables.main()
            elif group == 4:
                conditions.main()
            elif group == 5:
                basic_math.main()
            elif group == 6:
                while_loop.main()
            #elif group == 7:
            #    lists.main()

            break
        except ValueError:
            print('Please enter a number')

main()
