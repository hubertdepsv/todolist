# Create a generator function that yields numbers from 1 to 5.

def number_generator():
    for number in range(1, 6):
        yield number

for number in number_generator():
    print(number)