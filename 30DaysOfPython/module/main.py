from mymodule import generate_full_name as full_name, sumofnum1num2 as sum, gravity as g, person as p
from math import pi, sqrt, pow, floor, ceil, log10
import string
from random import random, randint
from mymodule import random_user_id as id
import os
print(os.listdir('30DaysOfPython'))
if os.path.exists('30DaysOfPython/function_P.py'):
    print('file exists')
else:
    print('file not found')
print(full_name('christian', 'san joaquin'))
print(sum(1, 8))
mass = 100
weight = mass * g
print(weight)
print(p['taste'])
print(pi)
print(sqrt(8))
print(pow(5, 1))
print(floor(6.67))
print(ceil(6.67))
print(log10(100))

print(string.ascii_letters + string.digits)
print(string.digits)
print(string.punctuation)
print(ord('A'))
print(chr(65))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(random()) # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(1, 100)) # it returns a random integer number between [5, 20] inclusive

n = string.ascii_lowercase + string.digits
length = len(n)
random = randint(0, length - 1)
one_char = n[random]
print(one_char)
print(id())
