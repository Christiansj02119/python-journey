it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
a_b = a.symmetric_difference(b)
age = [22, 19, 24, 25, 26, 24, 25, 24]
lengthH_it_companies = len(it_companies)
it_companies.add('Twitter')
it_companies.update(['Netflix', 'Sulasok', 'Porn'])
it_companies.remove('Porn')
print(it_companies)
it_companies.discard('Facebook')
print(it_companies)
print(a_b)