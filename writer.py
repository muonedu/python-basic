import string
import random

filename = 'test.txt'

f = open(filename, 'a')

for i in range(1000000):
    s = list(string.ascii_lowercase)
    random.shuffle(s)
    k1 = "".join(s[::4])
    k2 = "".join(s[::6])
    k3 = "".join(s[::8])
    fs = k1 + " " + k2 + " " + k3 + "\n"
    f.write(fs)

f.close()


