# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dick = {
    'first_name':'christian',
    'last_name':'san joaquin',
    'age':69,
    'country':'philippines',
    'singol':True,
    'height':1.70,
    'skill':['python', 'java', 'c++', 'html', 'css', 'mySql'],
    'address':{
        'barangay':'abo',
        'city':'camarines sur'
    }
}
dick_copy = dick.copy()
dick_keys = dick.keys()
dick_values = dick.values()

print(len(dick))
print(dick['singol'])
print(dick['skill'])
print(dick['skill'][0])
print(dick['address']['city'])
print(dick.get('handsome'))
dick['skill'].append('myPhp')
print(dick['skill'])
dick['weight'] = 800
print(dick['weight'])
print(dick['first_name'])
dick['first_name'] = 'Kopal'
print(dick['first_name'])
print('weight' in dick)
print(dick)
dick.popitem()
print(dick)

print(f"{dick['height']:.2f}")