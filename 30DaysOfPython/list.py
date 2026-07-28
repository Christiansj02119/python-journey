
lst = ['bossatan', 'darryl', 'tungtung', 'christian', 'boy']
a, b, c, *rest = lst
print('names:', a, b, c)
print('number of names:', len(lst))
print('length of names:', len(lst[0]), len(lst[1]), len(lst[2]))
print('reserve list:', rest)
print("number of names:", len(rest))

fruits = ['banana', 'orange', 'mango', 'lemon']
a = fruits[0:2]
b = fruits[::2]
fruits_copy = fruits.copy()
fruits.pop()
fruits.append('pineapple')
fruits.remove('banana')
fruits.insert(1, 'betlog')
fruits.pop(2)
print('before change:', fruits_copy)
print('after change:', fruits)
#del fruits
#fruits.clear()
#print(fruits)
combined = fruits_copy + fruits
print(combined)
#other way to combine
#fruits_copy.extend(fruits)
#print(fruits.count('betlog'))
#print(fruits.index('betlog'))
#fruits.reverse()
#print(fruits)
#fruits.sort()
#print(fruits)
#fruits.sort(reverse=True)
#print(fruits)
#result = sorted(fruits)