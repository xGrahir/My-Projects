import random


def random_with_sum(number_of_values, asserted_sum):
    trial = 0
    numbers = list(range(number_of_values))
    while True:

        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1, 101)

        if sum(numbers) == asserted_sum:
            yield ((trial, numbers))
            trial = 0

a = random_with_sum
for i in range(10):
    (number_of_trials, numbers) = next(a(3, 100))
    print(number_of_trials, numbers)