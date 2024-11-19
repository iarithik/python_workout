def how_many_diff_numbers(num):
    unique_num = set(num)
    return unique_num, len(unique_num)

op = how_many_diff_numbers( [1, 2, 3, 1, 2, 3, 4, 1])
print(op)