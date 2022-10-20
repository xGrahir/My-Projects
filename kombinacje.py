import itertools
import math

mylist = ["a", "b", "c", "d"]
list_to = []
for a in mylist:
    for b in mylist:
        for c in mylist:
            if a == b:
                pass
            elif b == c:
                pass
            elif a == c:
                pass
            else:
                list_to.append((a, b, c))

print("-"*100)
lista = []
for permut in itertools.permutations(mylist, 3):
    lista.append(permut)

money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
money_100 = []

for i in range(1, 101):
    for combination in itertools.combinations(money, i):
        if sum(combination) == 100:
            print(combination)

print("-"*100)
notes = ["C", "D", "E", "F", "G", "A", "B"]
mynotes = []
for combination in itertools.product(notes, repeat=4):
    print(combination)

n = len(notes)
k = 4

V = pow(n, k)
print(V)
V = (math.factorial(n))/(math.factorial(n-k))
print(V)
