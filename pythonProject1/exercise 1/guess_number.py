import random

my_number = random.randint(1,10)

chance = 4
active = True

while active:
    user_number = int(input('Guess a number: '))
    if user_number == my_number:
        print('You won!!!')
        break
    elif user_number < my_number:
        print('Number is too low')
        print(f'you have {chance} chance left')
        chance -= 1
    else:
        print('Numer is too high')
        print(f'you have {chance} chance left')
        chance -= 1
    if chance == 0:
        active = False
