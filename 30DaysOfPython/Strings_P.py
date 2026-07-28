first_name = 'boyoy boy'

for item in first_name:
    if item == first_name[1]:
        break
    else:
        print(item)
temp = first_name[0:3]
print(temp)
print(first_name[-1:-4:-1])
sum = [1, 3, 3, 4, 5, 6, 1]
print(sum.count(3))
print(first_name.count('y'))
print(first_name.endswith('yoy'))
print(first_name.startswith('boy'))
print(first_name.replace('boy', 'kopal'))
print(first_name.rfind('y'))