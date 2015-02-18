class SortedDict(dict):
    def __str__(self):
        return "{%s}" % ", ".join([str(u) + ": '" + str(v) + "'"
                                   for u, v in sorted(self.iteritems(),key=lambda x: x[0])])

d = SortedDict(d)
print d
