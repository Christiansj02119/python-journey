print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('A' in 'christiAn')
print('poca' not in 'christian')

letter = 'K'
print(len(letter))
word = 'christian'
print(len(word))

first_name = 'christian'
last_name = 'san joaquin'
age = 19
full_name = first_name + ' ' + last_name
paragraph = '''I am a \"teacher\" and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print('This is my full name {} and I am {} years old ' .format(full_name, age))
print(paragraph)
print(' length of first name:', len(first_name), '\n', 'length of last name:', len(last_name))

print('boy\tcat\tdog\ttomboy')

firstname = 'Asabeneh'
lastname = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}, I teach {}' .format(firstname, lastname, language)
print(formated_string)

a = 5
b = 1 
print(f'{a} + {b:.5f} = {a + b}')

language = 'Piathong'
first_letter = language[-2]
second_letter = language[1]
third_letter = language[7]
fourth_letter = language[2]
slice1 = language[0:4]
slice2 = language[4:8]
print(first_letter, second_letter, third_letter, third_letter, fourth_letter)
print(slice1 + slice2)
print(language[::-1])
print(language[0:6:2])
x = 'christian'
print(x.capitalize())


challenge = 'thirty\tdays\tof\tpython'
z = 'python'
o = 'thirty'
print(challenge)
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 18 ))
print(challenge.endswith('tian'))
print(challenge.expandtabs(20))
print(challenge.find('y'))
print(challenge.rfind('y'))
print(challenge.index(o))
print(challenge.index(z))
print(challenge.islower())

j = 'san joaquin'
n = 'SAN JOAQUIn'
print(j.strip('san'))
print(j.replace('joaquin', 'san'))
print(j.split())
print(n.swapcase())
print(j.startswith('san'))

