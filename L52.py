# The authors are Saerin Bong and Olivia Busk

def perfect_number(n):
    sum_divisors=0
    for x in range(1, n):
        if n % x==0:
            sum_divisors+=x
    if sum_divisors==n:
        return True
    else:
        return False

print(perfect_number(28))
print(perfect_number(1000))
print(perfect_number(10000))
