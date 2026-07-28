
num1 = 0
while num1 < 10:
    print(num1)
    num1 = num1 + 1
    if num1 == 5:
        print(num1)
        print('STOP')
        break

lst = [0, 1, 2, 3, 4, 5]
for item in lst:
    print(item)
else:
    print('STOP')
first_name = 'christian'
for item in first_name:
    print(item)

lst_name = ['christian', 'bossatan', 'lapo'] #lists
 
for i in lst_name:
    if i == 'bossatan':
        continue
    print(i)
else:
    print('STOP')

tpl = ('lolo', 'lola', 'idol') #tuples
for item in tpl:
    print(item)
else:
    print('STOP')

student = {
    'first_name':'christian',
    'last_name':'san joaquin',
    'student_id':202510876,
    'age':18,
    'enrolled':False
}
for item, value in student.items():
    print(item, value)

#it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#for item in it_companies:
#    print(item)

num5 = list(range(5, 16, 5))
print(num5)
num6 = list(range(15, 5, -2))
print(num6)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number1 in range(11):
    print(number1)
else:
    print('STOP', number1)