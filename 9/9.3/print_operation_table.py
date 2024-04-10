def print_operation_table(operation, x, y):
    for i in range(1,x+1):
        for j in range(1, y+1):
            print(operation(i, j),end=' ')
        print()

print_operation_table(pow, 5, 4)