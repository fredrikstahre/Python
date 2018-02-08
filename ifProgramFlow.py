# name = input('Please enter your name: ')
# age = int(input('How old are you, {0}? '.format(name)))
# print(age)
#
# if age >= 18:
#     print('You are old enough to vote!')
# else:
#     print('Please come back in {0} years'.format(18 - age))

# print('Please guess a number between 1 to 10: ')
# guess = int(input())
#
# if guess < 5:
#     print('Sorry, please guess higher.')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it!')
#     else:
#         print('Sorry, you have not guessed correctly.')
# elif guess > 5:
#     print('Please guess lower.')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, you guessed it!')
#     else:
#         print('Sorry, you have not guessed correctly.')
# else:
#     print('You got it first time!')

print('Please guess a number between 1 to 10: ')
guess = int(input())

if guess != 5:
    if guess < 5:
        print('Sorry, please guess higher.')
    else: # guess must be greater than 5
        print('Please guess lower')

    guess = int(input()) # give the user another try
    if guess == 5:
        print('Well done, you guessed it!')
    else:
        print('Sorry, you have not guessed correctly.')
else:
    print('You got it first time!')