import math

age = int(input('Enter an age here.'))

category = '60+'

if age < 13:
    category = 'child'
elif age < 20:
    category = 'Teenager'
elif age < 60:
    category = 'Adult'

print(f'This person belongs to the category of {category} age group.')
