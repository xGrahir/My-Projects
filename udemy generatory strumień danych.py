import random

def random_with_sum(number_of_sum, asserted_sum):
    trial = 0
    numbers = []
    while True:

        trial += 1
        for i in range(number_of_sum):
            a = random.randint(1, 101)
            numbers.append(a)

        if sum(numbers) == asserted_sum:
            yield trial, numbers
            trial = 0
        else:
            numbers.clear()
            continue

for i in range(10):
    (trials, number) = (next(random_with_sum(3, 100)))
    print(trials, number)
