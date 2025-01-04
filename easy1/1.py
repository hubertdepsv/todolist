# Create a list where each number from the original list is squared using the map method.

lst = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, lst)
print(list(squared))