def reciprocals(n):
    for number in range(1, n + 1):
        yield 1 / number

for number in reciprocals(10):
    print(number)