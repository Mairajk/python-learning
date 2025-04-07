pet = input('Enter your pet here:').lower()

if pet not in ['cat', 'dog']:
    print('You can only enter "cat" or "dog" in the pet.')
    exit()

age = float(input("Enter your pet's age here:"))

if pet == 'cat':
    if age <= 5:
        food_type = 'kitten'
    else:
        food_type = 'cat'
elif pet == 'dog':
    if age < 2:
        food_type = 'puppy'
    else:
        food_type = 'dog'

print(f'You should give {food_type} food to your {pet}.')
