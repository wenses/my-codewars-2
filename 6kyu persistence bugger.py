def mp(n):
    global count
    count+=1
    if len(str(n))==1:
        return count-1
    else:
        ans=1
        
        for c in str(n):
            ans*=int(c)

        return mp(ans)


count=0
print(mp(25))
    
    
     
