import os
import itertools

def scantree(path):
    scan = os.scandir(path)
    for s in scan:
        if os.path.isdir(s) is True:
            yield s
            yield from scantree(s.path)
        else:
            yield s


path = r"C:\Users\tomas\PycharmProjects\My-Projects"
listing = scantree(path)
for list in listing:
    print("Dir" if list.is_dir() else "File", list.path)


# listing = scantree(path)
#
# listing = sorted(listing, key=lambda e: e.is_dir())
#
# for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
#     print('DIR ' if is_dir else 'FILE', len(list(elements)))