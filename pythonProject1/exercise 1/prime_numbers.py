for number in range(1, 101):

    if number % 15 == 0:
        print('Fizz\nBurz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Burz')
    else:
        print(number)
    number += 1
