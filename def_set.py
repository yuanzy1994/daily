
strings = ('puppy', 'kitten', 'puppy', 'puppy',
           'weasel', 'puppy', 'kitten', 'puppy')

count={}

for s in strings:
    count.setdefault(s,0)
    count[s] += 1
print count




from collections import defaultdict

dd = defaultdict(list)
print  type(dd)

dd['name']
print dd

dd['age'].append('18')
print dd

dd['age'].append('20')
print dd



