
def dr(n:str):
    if len(str(n))==1:
        return n
    else:
        ans=0
        for c in str(n):
            ans+=int(c)
        return dr(ans)

print(dr('564'))


     
