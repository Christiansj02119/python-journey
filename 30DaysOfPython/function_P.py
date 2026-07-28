import math

def addtwonum(num1, num2):
    sum = num1 + num2
    return sum
print(addtwonum(5, 1))
def Area_of_circle(radius):
    area = math.pi * radius ** 2
    return area
print(Area_of_circle(10))

"""def add_all_nums(num):
    sum = 0
    for item in num:
        if type(item) == int:
            sum += item
        elif type(item) == str:
            continue
    return sum
mylist = [1, 2, 3, 'christian masarap', 4]
for item in mylist: 
    if type(item) == int:
        add_all_nums(mylist)
    elif type(item) == str:
        print(item)
    else:
        print('kopal')
print(add_all_nums(mylist))"""

def addallnum(*nums):
    sum = 0
    total = ''
    for item in nums:
        if type(item) == int:
            sum += item
        elif type(item) == str:
            total += item + ' '
    print(total)
    return sum
    
print(addallnum(1, 2, 3, 'kopal', 4, 5, 'kaba'))

def convert_celsius_to_fahrenheit(celcius):
    farenheit = celcius * 9/5 + 32
    return farenheit
faren = convert_celsius_to_fahrenheit(24)
print(f'convert celcius to farenheit: °{faren}')

def check_session(user_input):
    autumn = [9, 10, 11]
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    if user_input in autumn:
        print('autumn')
    elif user_input in winter:
        print('winter')
    elif user_input in spring:
        print('spring')
    elif user_input in summer:
        print('summer')

user_input = int(input('Enter the month to check the season:'))
check_session(user_input)

def calculate_slope(y2, y1, x2, x1):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(calculate_slope(x1=1, x2=5, y1=2, y2=4))


def is_prime(n):
    if n < 2:
        return False
    for item in range(2, int(n ** 0.5) + 1):
        if n % item == 0:
            return False
    return True
for item in range(1, 50):
    if is_prime(item):
        print(item)