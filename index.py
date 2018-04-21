'''
records = [('foo',1,2),('bar','hello'),('foo',3,4),]

def  do_foo(x,y):
    print ('foo',x,y)

def do_bar(arg):
    print ('bar',arg)

for tag,*arg in records:
    if tag == 'foo':
        do_foo(*arg)
    elif tag == 'bar':
        do_bar(*arg)
'''


'''
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

uname,*fields,homedir,sh = line.split(':')
print (uname)
print (*fields)
print (homedir)
print (sh)
'''

'''
items = [1, 10, 7, 4, 5, 9]
def sum_arg(items):
    head,*tail = items
    return head+sum(tail) if tail else head
print (sum_arg(items))
'''

'''
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print (i)
'''

# def creategenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
# mygenerator = creategenerator()
# print (mygenerator)
# for i in mygenerator:
#     print (i)


# from collections import deque
#
# def search(lines,pattern,history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line,previous_lines
#         print ('line:',line)
#         print ('previous_lines',previous_lines)
#
#
#         previous_lines.append(line)
#
# if __name__ == '__main__':
#     with open(r'pattern.txt') as f:
#         for line,prevlines in search(f,'hello',5):
#             for pline in prevlines:
#                 print (pline,end='')



# import heapq
# nums = [1,8,2,23,7,-4,18,43,47,2]
# print (heapq.nlargest(3,nums))
# print (heapq.nsmallest(3,nums))
# heap = list(nums)
# heapq.heapify(heap)
# print (heap)
# for i in heap:
#     print (heapq.heappop(heap))
#
#
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print (heapq.nsmallest(2,portfolio,key=lambda s:s['price']))

#
# import heapq
# heap = [1,2,3,4,5,6,7,8,9,10]
# heapq.heappush(heap,100)
# print  (heap)
# for i in range(10):
#     heapq.heappop(heap)
# print  (heap)

# import heapq
# def  heapsort(iterable):
#     h = []
#     for value in iterable:
#         heapq.heappush(h,value)
#     print (h)
#     return [heapq.heappop(h) for i in range(len(h))]
# print (heapsort([1,3,5,7,9,2,4,6,8,0]))


# import heapq
# def HeapSort(list):
#     heapq.heapify(list)
#     heap = []
#     while list:
#         heap.append(heapq.heappop(list))
#     list[:] = heap
#     return list
# print (HeapSort([1,3,5,7,9,2,4,6,8,0]))


# from collections import defaultdict
# d =defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# print (d.items())


# from collections import OrderedDict
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
# # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
# for key in d: print(key, d[key])


# prices = {
#     'ACME': 45.23,
#     'AAPL': 612.78,
#     'IBM': 205.55,
#     'HPQ': 37.20,
#     'FB': 10.75
# }
#
# key_list = prices.keys()
# value_list = prices.values()
# print (key_list)
# print (value_list)
# zi = zip(key_list,value_list)
# print (zi)


# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
# a = [1,5,6,2,1,9,5,10]
# de_list = list(dedupe(a))
# print (de_list)


# a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# b = {'x':100}
# print (b['x'])
# def dedupe(items,key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield val
#             seen.add(val)
# print (list(dedupe(a,key=lambda d: (d['x'],d['y']))))


# s = 'HelloWorld'
# a = slice(5,50,2)
# ind = a.indices(len(s))
# print (ind)
# print (*a.indices(len(s)))
# print (range(*a.indices(len(s))))


# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
#     'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
#     'my', 'eyes', "you're", 'under'
# ]
#
# from collections import Counter
# word_counts = Counter(words)
# top_three = word_counts.most_common(3)
# print  (word_counts)
# print (top_three)
#
# more_words = ['why','are','you','not','looking','in','my','eyes']
# for word in more_words:
#     word_counts[word] += 1
# print (word_counts['eyes'])
#
# word_counts.update(more_words)
# print (word_counts)



# rows = [
#     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
#     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
#     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
#     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
#
# from operator import itemgetter
# rows_by_fname = sorted(rows,key=itemgetter('fname'))
# rows_by_uid = sorted(rows,key=itemgetter('uid'))
# rows_by_any = sorted(rows,key=itemgetter('fname','lname'))
# print (rows_by_fname)
# print (rows_by_uid)
# print (rows_by_any)



# class User:
#     def __init__(self,user_id):
#         self.user_id =  user_id
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
# def sort_notcompare():
#     users = [User(23),User(3),User(99)]
#     print (users)
#     print (sorted(users,key=lambda u: u.user_id))
#
# sort_notcompare()
#
# from operator import attrgetter
# users = [User(23), User(3), User(99)]
# a = sorted(users,key=attrgetter('user_id'))
# print (a)


# rows = [
#     {'address': '5412 N CLARK', 'date': '07/01/2012'},
#     {'address': '5148 N CLARK', 'date': '07/04/2012'},
#     {'address': '5800 E 58TH', 'date': '07/02/2012'},
#     {'address': '2122 N CLARK', 'date': '07/03/2012'},
#     {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
#     {'address': '1060 W ADDISON', 'date': '07/02/2012'},
#     {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
#     {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# ]
# from operator import itemgetter
# from itertools import groupby
# rows_by_date = sorted(rows,key=itemgetter('date'))
# print  (rows_by_date)
#
# for date,items in groupby(rows,key=itemgetter('date')):
#     print (date)
#     for item in items:
#         print ('',item)


# from  collections import defaultdict
# rows_by_date2 = defaultdict(list)
# for row in rows:
#     list_row = rows_by_date2[row['date']].append(row)
# for i in rows_by_date2['07/01/2012']:
#     print (i)


# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
# ivals = list(filter(is_int,values))
# print (ivals)


# from  collections import namedtuple
# subscriber = namedtuple('a',['addr','joined'])
# sub  = subscriber('jonesy@example.com', '2012-10-19')
# print (sub)
# print (sub.addr)
# print (sub.joined)


# import  re
# datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# print  (datepat.findall(text))
# for month,day,year in datepat.findall(text):
#     print ('{}-{}-{}'.format(year,month,day))
# m = datepat.match('11/27/2012')
# print (m.group(0))
# print (m.group(1))
# print (m.groups())


# import  re
# text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# reSub = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
# print (reSub)


# s1 = ' hello world \n'
# print (s1.strip())
#
# s2 = ' hello world \n'
# print (s2.lstrip())
# print (s2.lstrip())
#
# s3 = '----hello world====='
# print (s3.strip('-'))
# print (s3.strip('-='))
#
# s4 = '---hello.world==='
# print (s4.strip('---').replace('.','!'))
#
# import re
# s5 = ' hello world \n'
# print (s5.replace(' ',''))
# print (re.sub(' ','',s5))


# with open(r'server.py') as f:
#     lines = (line.strip() for line in f)
#     print (lines)
#     for line in lines:
#         if line == '':
#             continue
#         else:
#             print (line)


# name = 'yuan'
# n = 100
# import string
# s = string.Template('$name has $n messages.')
# res = s.substitute(vars())
# print (res)


# s = 'Elements are written as "<tag>text</tag>".'
# import html
# print (s)
# print (html.escape(s))
# print (html.escape(s,quote=False))


# class Node:
#     def __init__(self,value):
#         self._value = value
#         self._children = []
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#     def add_child(self,node):
#         self._children.append(node)
#     def __iter__(self):
#         return iter(self._children)
#
# if __name__ == '__main__':
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     root.add_child(child1)
#     root.add_child(child2)
#
#     for ch in root:
#         print (ch)


# def frange(start,stop,increment):
#     x = start
#     while x < stop:
#         yield x
#         x += increment
#
# res = list(frange(0,2,0.5))
# print (res)

def countdown(n):
    print ("num",n)
    while n > 0:
        yield n
        n -= 1
    print ('Done!')
c = countdown(5)
print (c)
print (next(c))
print (next(c))
print (next(c))
print (next(c))
print (next(c))
print (next(c))













