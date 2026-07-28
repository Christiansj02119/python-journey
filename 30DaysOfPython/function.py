def greet(first_name):
    print('helo, ' + first_name)
def multiply(a, b):
    return a * b
def temp():
    first_name = 'christian'
    last_name = 'san joaquin'
    spacve = ' '
    print(first_name + spacve + last_name)
def addition():
    a = 5
    b = 1
    result = a + b
    return result
def string():
    first_name = 'christian'
    last_name = 'san joaquin'
    spacve = ' '
    full_name = first_name + spacve + last_name
    return full_name
def return1(course):
    temp = course + ' ' + 'masarap'
    return temp
def return2(age):
    eligible = 18
    if age >= 18:
        return 'eligible'
    else:
        return 'not eligible'
def area(aoc):
    pi = 3.14
    area = pi * aoc **2
    return area
def return3(n):
    total = 0
    for item in range(n+1):
        total += item
    return total
def full_name(first_name, last_name):
    space = ' '
    result = first_name + space + last_name
    return result
def eveorodd(number):
    if number % 2 == 0:
        return 'EVEN'
    return 'ODD'
def greetings(name = 'chupa'):
    message = name + ' ' + 'masarap'
    return message
def return4(*args):
    for item in args:
        print(item)
def return5(name, location):
    print('Hi im', name, 'my address is', location)

my_dict = {"name": "Alice", "location": "New York"}

return5(**my_dict)  

return5(name='christian', location='purok singko')




"""user_numbers = input('Enter num1 num2 num3: ')
numbers = tuple(int(item.strip()) for item in user_numbers.split(','))
for item in numbers:
    print(eveorodd(item))
"""
