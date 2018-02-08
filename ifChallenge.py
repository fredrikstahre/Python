name = input('Write your name: ')
age = int(input('How old are you? '))

# my solution
print('Hello {}'.format(name))
if (age >= 18) and (age < 31):
    print('Welcome to the holiday!')
else:
    print('Sorry, you must be between 18 and 31 years old.')

# Suggested solution
# name = input('Please enter your name: ')
# age = int(input('How old are you, {0}? '.format(name)))

# if 18 <= age < 31:
#   print('Welcome to club 18-30 holidays, {0}'.format(name))
# else:
#   print('Sorry, our holidays are only for seriously cool people.')
