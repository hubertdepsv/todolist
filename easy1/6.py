# Use reduce to concatenate a list of strings into a single string.
from functools import reduce
print(reduce(lambda x, y: x + y, ['a', 'b', 'c']))