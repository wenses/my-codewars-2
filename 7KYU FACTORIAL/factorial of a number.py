def factorial(n):
    
    if n>=0 and n<=12:
        f=1

        for i in range(1,n+1):
            f*=i
    else:
        raise ValueError
            
    
    return f

print(factorial(4))