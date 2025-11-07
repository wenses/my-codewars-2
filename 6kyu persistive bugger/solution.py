
def persistence(n):
    n0,a=str(float(n)).split('.')
    a=int(a)
    if len(str(n0))==1:
        return a
    else:
        ans=1
        
        for c in str(n0):
            ans*=int(c)
        a+=1
        print(a)
        return persistence(str(ans)+'.'+str(a))




print(persistence(999))
