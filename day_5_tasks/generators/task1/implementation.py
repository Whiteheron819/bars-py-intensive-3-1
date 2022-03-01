def fib(num):
    first_num, second_num = 1, 1
    for _ in range(0, num):
        yield first_num
        first_num, second_num = second_num, first_num + second_num

