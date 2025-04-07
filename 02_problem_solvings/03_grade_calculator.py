import math

score = float(input('Enter your grade here:'))


if score > 100:
    print('Grade should be less than or equal to 100.')
    exit()

grade = 'F'

if score > 80:
    grade = 'A+'
elif score > 60:
    grade = 'A'
elif score > 50:
    grade = 'B'
elif score > 40:
    grade = 'C'

print(f'Your grade is {grade}.')
