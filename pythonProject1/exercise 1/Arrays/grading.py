def load_data(rows, col):
    scores = []
    row_counter = 0
    while row_counter < rows:
        column_counter = 0
        print()
        print(f'student{row_counter + 1}')
        while column_counter < col:
            scores.append(int(input(f'subject{column_counter + 1} score: ')))
            print()
            column_counter += 1
        row_counter += 1
    return scores
