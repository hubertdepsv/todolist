strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def generate_capitalized(strings):
    for word in strings:
        yield word.capitalize()

print(tuple(generate_capitalized(strings)))