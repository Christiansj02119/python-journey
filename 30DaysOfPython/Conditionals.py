try:

    print('enter a number to determine if its higher or lower')
    a_input = int(input('numA:'))
    b_input = int(input('numB:'))

    if a_input > b_input:
        if a_input % 2 == 0:
            print('A is higher and its an even number')
        else:
            print('A is higher and its an odd number')
    elif a_input == b_input:
        if a_input == b_input % 2 == 0:
            print('A and B has the same integer and its both even number')
        else:
            print('A and B has the same integer and its both odd number')
            
    else:
        if b_input % 2 == 0:
            print('B is higher and its an even number')
        else:
            print('B is higher and its an odd number')
except ValueError:
    print('enter a valid number')