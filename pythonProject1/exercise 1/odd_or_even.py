import time
import os

dividend = int(input('Enter dividend: '))
divisor = int(input('Enter divisor: '))
start = time.time()
divider = divisor
count = 0;
active = True#
while active:
    if dividend >= divisor:
        divisor += divider
        count += 1
    else:

        active = False
os.system('exit')
print(count)
print(time.time()-start)
