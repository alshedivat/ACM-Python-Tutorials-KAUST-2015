class trace(object):
    def __init__(self, func):
        self.indent = 0
        self.func = func
    
    def __call__(self, *args):
        print "    "*self.indent + \
              "Calling %s with arguments (%s)" % (self.func.__name__, ','.join(map(str,args)))
        self.indent += 1
        result = self.func(*args)
        self.indent -= 1
        return result

@trace
@memoize
def Fib(n):
    """Return the n-th Fibonacci number."""
    assert type(n) is int and n >= 0, "ERROR (Fib): index should be positive and integer!"
    return Fib(n-1) + Fib(n-2) if n > 1 else 1 if n is 1 else 0
