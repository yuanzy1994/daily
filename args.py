
'''
records = [('foo',1,2),('bar','hello'),('foo',3,4),]

def do_foo(x,y):
    print ('foo',x,y)

def do_bar(s):
    print ("bar",s)

for tag,*args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)
'''


'''
line = 'root:*:0:0:System Administrator:/var/root:/bin/sh'
uname,*args,home_dir,sh = line.split(':')

print (uname,home_dir,sh)
'''


'''
record = ('ACME', 50, 123.45, (12, 18, 2012))

name,*_,(*_,year) = record

print  (year)
'''


'''
import  heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print (heapq.nlargest(3,nums))
print (heapq.nsmallest(3,nums))
'''


'''
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import  heapq
heap = list(nums)
heapq.heapify(heap)
print (heap)
'''

'''
from collections  import  defaultdict
d1 = defaultdict(list)
d1['a'].append(1)
d1['a'].append(2)
d1['a'].append(3)

d2 = defaultdict(set)
d2['b'].add(1)
d2['b'].add(2)
d2['b'].add(3)

print (d1,d2)
'''




