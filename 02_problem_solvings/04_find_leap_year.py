year = int(input('Enter the year here:'))


if not (year % 400) or (not (year % 4) and (year % 100)):
    print(f'The {year} is a leap year.')
else:
    print(f'The {year} is not a leap year.')

# or we can also do this in one line by using ternary

print(f'The {year} is {"" if not (year % 400) or (not (year % 4) and (year % 100)) else "not "}a leap year.')
