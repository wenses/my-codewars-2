def duration(n):
    def p1(secs):
        seconds=secs%60
        mins=(secs-seconds)/60
        return [mins,seconds]

    print(p1(60))
    #for above a minute
    if n<60:
        print(n)
    elif n>60 and n<3600:
        print(p1(n))

    elif n>3600 and n<86400:
        secs=n%3600
        hr=(n-secs)/3600

        rl=p1(secs)

        rl.insert(0,hr)
        print(rl)
        

    elif n>86400:
        secs=n%86400
        
        days=(n-secs)/86400

        s2=secs%3600
        
        hr=(secs-s2)/3600

        print(f'seconds {secs}')

        rl=p1(secs)

        rl.insert(0,hr)
        rl.insert(0,days)

        print(rl)
    else:
        print(p1(n))
    
        


duration(15731080)
