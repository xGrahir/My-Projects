zdanie = "mama.tata.wujek.ciocia"

def change_sentence(zdanie):
    return zdanie.replace('.', '[.]')

print(change_sentence(zdanie))

without = zdanie.split('.')
sep = "[.]"
together = sep.join(without)
print(together)
