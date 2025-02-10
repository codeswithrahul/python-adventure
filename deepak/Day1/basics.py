# swap two number 
a = 5
b = 6

def swap(a,b):
    c = a + b
    a = c - a
    b = c - b
    return a,b
    
print(swap(a,b))

# largest three number 
a = 4
b = 6
c = 13