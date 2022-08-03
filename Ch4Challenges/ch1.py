# Accepts value from user
a = input("Enter a number and I will square it: ")

# Casts value to int
a = int(a)

def squared(n):
    """
    returns a ** 2
    param: int a
    """
    return n ** 2

# pass a as param to squared
b = squared(a) 

# print b
print(b)
