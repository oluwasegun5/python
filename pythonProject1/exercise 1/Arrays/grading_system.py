import grading

row = int(input("Number of students: "))
column = int(input('Number of courses: '))

score = []
total = []

grading.load_data(row, column)

print(' \n' * 30)
student = 'STUDENTS'
print(f'{student:<16}', end='')
for i in range(column):
    sub = ' '
    print(f'sub{i + 1}{sub:>6}', end='')

print('\n')

for i in range(row):
    print(f'Student{i + 1}', end=' ')
    for j in range(column):
        print(f'{score[j]:>10}', end='')
    print()


def total():
    print('Total')
