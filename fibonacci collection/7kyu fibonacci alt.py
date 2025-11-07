
def fib(n:int) -> int:
    
    a=0
    b=1
    nf=0

    if n==1:
        nf=1
    
    for i in range(1,n):
        nf=a+b
        a=b
        b=nf

    return nf


for i in range(10):
    print(fib(i))
