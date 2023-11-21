def max_sum_dig(n_max, max_sum):
    count = 0
    mid = 0
    total = 0
    pas_list = []
    for i in range (1000, n_max+1):
        pass
        # first check number for conditions
            # разделить число на цифры по д1 д2 д3
        if i < 1000:
            d1 = i // 1000
            d2 = i / 100 % 10
            d3 = i / 10 % 10
            d4 = i % 10
            # проверить условие
        elif 1000 < i < 10000:
            d1 = i // 10000
            d2 = i / 1000 % 10
            d3 = i / 100 % 10
            d4 = i / 10 % 10
            d5 = i % 10
        elif 10000 < i < 100000:
            d1 = i // 100000
            d2 = i / 10000 % 10
            d3 = i / 1000 % 10
            d4 = i / 100 % 10
            d5 = i / 10 % 10
            d6 = i % 10

        if d1+d2+d3+d4 <= max_sum:

        # yes - total + i, count +1
        # find mid
        #
    return count, mid, total


print(list(max_sum_dig(2000, 4)))