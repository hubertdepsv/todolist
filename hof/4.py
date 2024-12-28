def reduce(callback, iterable, start):
    accum = start

    for item in iterable:
        accum = callback(item, accum)

    return accum

numbers = [3, 7, 2, 9, 5]
squares_sum = lambda number, accum: accum + number ** 2
print(reduce(squares_sum, numbers, 0))        # 168