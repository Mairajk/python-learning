import datetime

age = int(input('Enter the age here: '))

today = datetime.datetime.now().strftime("%A")

print(f'Today is {today} and your age is {age}.')

price = 12 if age >= 18 else 8

if today == 'Wednesday':
    price -= 2

print(f"Now ticket price for you is ${price}.")
