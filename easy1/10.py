# Create a generator function that yields user input strings until the word "stop" is entered.

def generate_strings():
    while True:
        s = input('Enter a string: ')
        if s == 'stop':
            break
        yield s
        
for user_input in generate_strings():
    print(user_input)