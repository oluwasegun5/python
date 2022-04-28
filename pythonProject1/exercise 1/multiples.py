import os

row = int(input('how many students: '))
column = int(input('how many courses: '))

score = [int(input(f'student{i+1} score{k+1}: ')) for i in range(0,row) for k in range(0,column)]
os.system('clear')

k = [print(i,end=' ') for i in score]