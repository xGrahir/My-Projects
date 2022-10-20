import random

def generator(how_much, max_number):

    lista = list(range(how_much))

    tries = 0
    while True:
        tries += 1
        for i in range(how_much):
            lista[i] = random.randint(1, 101)

        if sum(lista) == max_number:
            yield tries, lista


for i in range(10):
    (tries, lista) = next(generator(3, 100))
    print(tries, lista)