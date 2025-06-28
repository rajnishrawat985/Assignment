def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f
num = 5
print(f"Factorial of {num} is: ",fact(num))