# age = int(input('How old are you? '))

# AND stops as soon as something is false
# OR stops when something is true

# if (age >=16) and (age <=65):
# if 16 <= age <= 66:
# if 15 < age < 66:
#     print('Have a good day at work!')

# if (age < 16) or (age > 65):
#     print('Enjoy your free time!')
# else:
#     print('Have a good day at work!')
#
########################################
#
# This will print "x is true" beacuase the value of x is set
# if there's no value it will be false (0 = no value)
# x = 'false'
# if x:
#     print('x is true')

# x = input('Please enter some text: ')
# if x:
#     print('You entered "{}"'.format(x))
# else:
#     print('You did not enter anything.')

#########################################

# print(not False)
# print(not True)

#########################################

parrot = 'Norwegian Blue'

letter = input('Enter a character: ')

if letter in parrot:
    print('Give me an {}, Bob'.format(letter))
else:
    print("I don't need that letter")