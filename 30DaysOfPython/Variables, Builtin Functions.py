
# str to int or float
# Convert the string to a float first
# Then convert the float to an integer
num_str = '10.6'
numfloat = float(num_str)
numint = int(numfloat)
print('numint:', numint)
print('numfloat:', numfloat)
print(' ')
print(numfloat)
print(numint)

#str to list
first_name = 'christian'
last_name = 'san joaquin'
print('First name:', first_name)
first_name_to_list = list(first_name)
print('My first name in list: ', first_name_to_list)
print('length of my firstname:', len(first_name))
print('length of my lastname:', len(last_name))
print('total length of my whole name:', len(first_name) + len(last_name))
print(type(first_name))

num_one = int(input('num one: '))
num_two = int(input('num two: '))
total = num_one + num_two
print('num_one: ',num_one)
print('num_two: ', num_two)
print('total', total)





