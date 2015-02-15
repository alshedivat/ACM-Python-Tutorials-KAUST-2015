l = range(5,16,2)
print(l)

l[-1] = range(4,9,2)
print(l)

l[-1][-2] = -1
print(l)

del l[1:4]
print(l)

l.insert(1, 'Hello')
print(l)
