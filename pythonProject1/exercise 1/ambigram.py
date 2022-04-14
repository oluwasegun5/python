import math

counter = 1

for user_number in range(2, 10000000):

    power = user_number ** 2

    divisor = 10 ** (math.ceil(math.log10(user_number)))

    if power % divisor == user_number:
        print(f'{counter}  {user_number} is an ambigram of {power}')
        counter += 1
