
# Generators

def number_generator():
    for i in range(5):
        yield i

gen = number_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))