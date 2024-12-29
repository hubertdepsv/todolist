strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

capitalized = (word.capitalize() for word in strings if len(word) >= 5)

print(tuple(capitalized))