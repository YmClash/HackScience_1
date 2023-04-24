import random


random.seed("mOMO")


def print_random():
    num=[random.randint(0,100) for i in range(10)]
    print(f"les Nombre genere sont {num}")


print_random()

