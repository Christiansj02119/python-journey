import string
from random import randint
def generate_full_name(first_name, last_name):
    return first_name + ' ' + last_name
def sumofnum1num2(num1, num2):
    return num1 + num2
def random_user_id():
    n = string.ascii_lowercase + string.digits
    temp = []
    result = ''
    for item in range(0, 6):
        temp.append(randint(0, len(n) - 1))
    for item in temp:
        result += n[item]
        #print(n[item], end='')
    return result

gravity = 10    
person = {
    'first_name': 'christian',
    'last_name': 'san joaquin',
    'taste': 'masyarap'

}
