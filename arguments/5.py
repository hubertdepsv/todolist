def find_person(**kwargs):
    for key, value in kwargs.items():
        if key == "Antonina":
            return value
    
    return "Antonina not found"

print(find_person(Bob="Actor", Antonina="Teacher"))
print(find_person(Bob="Actor"))