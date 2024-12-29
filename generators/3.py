strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
capitalized = (word.capitalize() for word in strings)

print(tuple(capitalized))