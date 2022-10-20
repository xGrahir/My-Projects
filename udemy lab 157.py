import os
import requests


def get_gen_files(dir):
    get = os.listdir(dir)
    for g in get:
        file = os.path.join(dir, g)
        yield file


def gen_get_file_lines(filename):
    for file in filename:
        with open(file) as file:
            for f in file:
                yield f.rstrip("\n")


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200, url
    except:
        return False, url


path = r"C:\Users\tomas\PycharmProjects\My-Projects"
path2 = r"C:\Users\tomas\PycharmProjects\My-Projects\stronki"

a = get_gen_files(path2)
c = gen_get_file_lines(a)

dd = check_webpage("https://www.udemy.com")
print(dd)

for d in c:
    a, url = check_webpage(d)
    if a is True:
        print("adres {} is True".format(url))
    else:
        print("adres {} is False".format(url))

# try:
#     os.mkdir(path2)
# except:
#     pass
#
# a = os.path.join(path2, "pl.txt")
# b = os.path.join(path2, "com.txt")
#
# with open(a, 'w') as f:
#     f.write('http://www.wykop.pl/\n')
#     f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
#     f.write('http://www.demotywatory.pl')
#
# with open(b, 'w') as f:
#     f.write('http://www.realpython.com/\n')
#     f.write('http://www.nonexistenturl.com/\n')
#     f.write('http://www.stackoverflow.com')
