#Count Digits
def count_digits(n):
    n=abs(n)
    if n<10:
        return 1
    else:
        return 1+count_digits(n // 10)
print(count_digits(45645645))