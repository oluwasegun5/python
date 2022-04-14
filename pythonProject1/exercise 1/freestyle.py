number = int(input('Enter a number: '))

sum_of_factor = 0

counter = 1
while counter < number:

    if number % counter == 0:
        print(f'{counter} is a factor of {number}')
        sum_of_factor += counter
    counter += 1
print(f"The sum of the factors is {sum_of_factor}")

if sum_of_factor == number:
    print(f'{number} is a perfect number')
elif sum_of_factor > number:
    print(f'{number} is an abundant number')
else:
    print(f'{number} is a deficient number')
