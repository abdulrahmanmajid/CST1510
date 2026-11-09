n = 21 # this is stored globally

def double(n):
    n = n * 2
    return n # this is stored locally


print (double(n)) # = 42
print (n)  # = 21