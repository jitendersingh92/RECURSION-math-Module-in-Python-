
x = int(input('Enter a number: '))

def f(n):
    if n < 2 :
        return 1
    else:
        return n * (f(n-1))
result = f(x)
print('Factorial of',x,'is: ',result)
