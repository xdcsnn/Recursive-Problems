#Print Numbers from N to 1
def print_reverse(n):
    if n<1:
        return
    print(n)
    print_reverse(n-1)
print(print_reverse(21))