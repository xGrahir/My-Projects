import itertools as it

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

a = get_factors(20)
candidate_list = [i for i in range(1, 10001)]

filtered_list = it.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list)

for filtr in filtered_list:
    a = get_factors(filtr)
    print("Liczba {} posiada dzielniki {} i jest doskonała".format(filtr, a))