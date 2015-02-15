d = {'John Smith': 30,
     'Ahmad Said': 22,
     'Sara John': 2}
print(d)

john = 'John Smith'
d[john] = d[john] + 1
print(d)

d['Ahmad Ahmad'] = 19
print(d)

del d['Sara John']
print(d)
