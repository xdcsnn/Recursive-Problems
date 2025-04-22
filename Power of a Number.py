#Power of a Number
def power(a,b):
    if exponent==0:
        return 1
    else:
        return base*power(a,b-1)
print(power(2,3))
