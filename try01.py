import re
import time

s = "ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz"

print re.split(r'[;|,\t]+', s)

i = 0
while i < 10:
    try:
        i += 1
        a = [1, 2, 3, 4, 5]

        index_v1 = a[2]
        index_v2 = a[10]

    except IndexError, test:
        print "error", test

    else:
        print "ok!"
