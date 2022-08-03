def add(a, b, c, d=4, e=5):
    """
    This function has three optional
    paramaters and two optional parameters
    param: a: int
    param: b: int
    param: c: int
    param: d: int
    param: e: int
    returns a + b + c + d + e
    """
    return a + b + c + d + e

# call evoked to show use of initial paramaters
print(add(1,2,3))

# call evoked to show use of optional paramaters
print(add(1,2,3,8,9))
