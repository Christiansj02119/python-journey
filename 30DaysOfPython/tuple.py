muscle_parts = ('chest', 'back', 'legs', 'shoulder', 'calves')
day = ('monday', 'tuesday', ' wednesday', 'friday', ' saturday')
a = muscle_parts[0:3]
b = muscle_parts[-1]
all_muscleP = muscle_parts[0:]
lst = list(muscle_parts)
print('number of muscle parts:', len(muscle_parts))
print(a)
print(all_muscleP)
print(b)
lst.append('tricep')
lst.insert(2, 'bicep')
print('traps' in muscle_parts)
workout_program = muscle_parts + day
print(workout_program)  
#my_list = [1, 2, 3]      # square brackets
#my_tuple = (1, 2, 3)     # parentheses