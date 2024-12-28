def times(callback, count):
    return [callback(item) for item in range(count)]

times(lambda number: print(number**2), 5)
# 0
# 1
# 4
# 9
# 16

pets = ('cat', 'dog', 'fish', 'bearded dragon')
new_pets = []
times(lambda index: new_pets.append(pets[index].title()),
      len(pets))
print(new_pets)
# ['Cat', 'Dog', 'Fish', 'Bearded Dragon']