""""
#lists = []
#tuples = ()
#sets = {}
user_input = input('Enter body parts: ')
body_parts = user_input.split(',') 

work_days = {'monday', ' tuesday', 'wednesday', 'thursday', 'friday'}
workouts = {'chest', 'back', 'shoulder', 'legs', 'abs'}
length_of_days = len(work_days)
print(length_of_days)
work_days.add('saturday')
workout_program = work_days.union(workouts)
print(workout_program)

usir_input = input('Enter names: ')
names = tuple(item.strip() for item in usir_input.split(','))
print(names)

user_inpot = input('Enter numbers: ')
numbers = tuple(int(item.strip()) for item in user_inpot.split(','))
print(numbers)


num1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12}
num2 = {2, 4, 6, 8, 10}
num3 = num1.intersection(num2)
print(num1.intersection(num2))
print(num3)


print("saturday" in work_days)
print("sunday" in work_days)
work_days.update('sunday')
print("sunday" in work_days)
work_days.discard('sunday')
print("sunday" in work_days)
print(work_days)
#work_days.clear()
#del work_days
"""

user_num1 = input('enter whole numbers: ')
num1 = set(int(item.strip()) for item in user_num1.split(','))
user_num2  = input('enter even numbers: ')
num2 = set(int(item.strip()) for item in user_num2.split(','))

superset = num1.issuperset(num2)
subset = num2.issubset(num1)
print(superset)
print(subset)   
num1.update('')
print(num1.difference(num2))
print(num2.difference(num1))
print(num1.symmetric_difference(num2))
print(num2.symmetric_difference(num1))
print(num1.isdisjoint(num2))
print(num2.isdisjoint(num1))
