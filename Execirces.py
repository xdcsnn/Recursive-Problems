#Sum of Natural Numbers
def sum_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_natural(n - 1)

print(sum_natural(98))
