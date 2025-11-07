def format_duration(n):
    def p1(secs):
        seconds=secs%60
        mins=(secs-seconds)/60
        return [mins,seconds]
    def p2(x):
            secs=x%3600
            
            hr=(x-secs)/3600
            print(hr)

            rl=p1(secs)

            rl.insert(0,hr)

            return rl
    

    
    #for above a minute
    if n==0:
        rl="now"
    elif n<60:
        rl=n
    elif n>=60 and n<3600:
        rl=p1(n)

    elif n>=3600 and n<86400:
        rl=p2(n)
        

    elif n>86400 and n<31536000:
        secs=n%86400
        
        days=(n-secs)/86400

        s2=secs%3600
        
        hr=(secs-s2)/3600

        

        rl=p2(secs)

        rl.insert(0,days)

        
    elif n>=31536000:
        yr_rem=n%31536000

        yr=(n-yr_rem)/31536000

        sec_rem=yr_rem%86400

        days=(yr_rem-sec_rem)/86400

        rl=p2(sec_rem)
        rl.insert(0,days)
        rl.insert(0,yr)


    return list(map(int,rl))
   

def format_output(el):
    

    if len(el)==1:
        es=f'{el[0]} seconds'
    elif len(el)==2:
        if el[0]!=0:
            es=f''
    elif len(el)==3:
        if el[0]!=0:
            es+=el[0]+"hours"
    
        
print(format_duration(3662))

