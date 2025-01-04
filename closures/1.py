def create_greeting():
    greeting = 'Hello'
    other = "blob"
    print(hex(id(greeting))) # 0x1010114b0

    def display_greeting():
        print(greeting)
        print(other)

    return display_greeting

greet = create_greeting()
print(greet.__closure__)            # (<cell at 0x100feb070: str object at 0x1010114b0>,)
print(create_greeting.__closure__)  # None