d = {}
for w in words:
    if len(w) > 2:
        if len(w) in d:
            d[len(w)].append(w)
        else:
            d[len(w)] = [w]
print d
