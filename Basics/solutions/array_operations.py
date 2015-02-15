print('Part 1:')
print 10+np.arange(90)

print('\nPart 2:')
print np.nonzero([1,2,0,0,4,0])[0]

print('\nPart 3:')
chess = np.zeros((8,8))
chess[1::2,::2] = 1
chess[::2,1::2] = 1
print chess

print('\nPart 4:')
print np.fromfunction(lambda i, j: (i +1)* (j+1)**2, (5, 3), dtype=int)

print('\nPart 5:')
normal_dist = np.random.normal(3, 1.5, (4,4))
print normal_dist
print normal_dist.sum(axis=1)
