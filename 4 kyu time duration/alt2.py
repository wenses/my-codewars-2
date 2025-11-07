def format_duration(n):
    def p1(secs):
        seconds=secs%60
        mins=(secs-seconds)/60
        return [mins,seconds]
    def p2(x):
            secs=x%3600
            
            hr=(x-secs)/3600

            rl=p1(secs)

            rl.insert(0,hr)

            return rl
    

    
    #for above a minute
    if n==0:
        return "now"
    elif n<60:
        rl=[n]
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

    def format_output(el):
    
        if type(el)!=list:
            es=el
        elif len(el)==1:
            es=f'{f'{el[0]} seconds'if el[0]>1 else f'{el[0]} second'}'
        elif len(el)==2:
            if el[0]!=0 and el[1]!=0:
                es=f'{f'{el[0]} minutes'if el[0]>1 else f'{el[0]} minute'} and {f'{el[1]} seconds'if el[1]>1 else f'{el[1]} second'}'
            elif el[0]==0:
                es=f'{f'{el[1]} seconds'if el[1]>1 else f'{el[1]} second'}'
            elif el[1]==0:
                es=f'{f'{el[0]} minutes'if el[0]>1 else f'{el[0]} minute'}'
                
        elif len(el)==3:
            if el[0]!=0 and el[1]!=0 and el[2]!=0:
                es=f'{f'{el[0]} hours'if el[0]>1 else f'{el[0]} hour'},{f'{el[1]} minutes'if el[1]>1 else f'{el[1]} minute'} and {f'{el[2]} seconds'if el[2]>1 else f'{el[2]} second'}'
            elif el[0]==0:
                es=f'{f'{el[1]} minutes'if el[1]>1 else f'{el[1]} minute'} and {f'{el[2]} seconds'if el[2]>1 else f'{el[2]} second'}'
            elif el[1]==0:
                es=f'{f'{el[0]} hours'if el[0]>1 else f'{el[0]} hour'} and {f'{el[2]} seconds'if el[2]>1 else f'{el[2]} second'}'
            elif el[2]==0:
                es=f'{f'{el[0]} hours'if el[0]>1 else f'{el[0]} hour'} and {f'{el[1]} minutes'if el[1]>1 else f'{el[1]} minute'}'

        elif len(el)==4:
            if el[0]!=0 and el[1]!=0 and el[2]!=0 and el[3]!=0:
                es=f'{f'{el[0]} days'if el[0]>1 else f'{el[0]} day'},{f'{el[1]} hours'if el[1]>1 else f'{el[1]} hour'}, {f'{el[2]} minutes'if el[2]>1 else f'{el[2]} minute'} and {f'{el[3]} seconds'if el[3]>1 else f'{el[3]} second'}'
            elif el[0]==0:
                es=f'{f'{el[1]} hours'if el[1]>1 else f'{el[1]} hour'}, {f'{el[2]} minutes'if el[2]>1 else f'{el[2]} minute'} and {f'{el[3]} seconds'if el[3]>1 else f'{el[3]} second'}'
            elif el[1]==0:
                es=f'{f'{el[0]} days'if el[0]>1 else f'{el[0]} day'}, {f'{el[2]} minutes'if el[2]>1 else f'{el[2]} minute'} and {f'{el[3]} seconds'if el[3]>1 else f'{el[3]} second'}'
            elif el[2]==0:
                es=f'{f'{el[0]} days'if el[0]>1 else f'{el[0]} day'},  {f'{el[1]} hours'if el[1]>1 else f'{el[1]} hour'} and {f'{el[3]} seconds'if el[3]>1 else f'{el[3]} second'}'

            elif el[3]==0:
                es=f'{f'{el[0]} days'if el[0]>1 else f'{el[0]} day'}, {f'{el[1]} hours'if el[1]>1 else f'{el[1]} hour'} and {f'{el[2]} minutes'if el[2]>1 else f'{el[2]} minute'}'

        elif len(el)==5:
            if el[0]!=0 and el[1]!=0 and el[2]!=0 and el[3]!=0:
                es=f'{f'{el[0]} years'if el[0]>1 else f'{el[0]} year'},{f'{el[1]} days'if el[1]>1 else f'{el[1]} day'}, {f'{el[2]} hours'if el[2]>1 else f'{el[2]} hour'}, {f'{el[3]} minutes'if el[3]>1 else f'{el[3]} minute'} and {f'{el[4]} seconds'if el[4]>1 else f'{el[4]} second'}'
            elif el[0]==0:
                es=f'{f'{el[1]} days'if el[1]>1 else f'{el[1]} day'}, {f'{el[2]} hours'if el[2]>1 else f'{el[2]} hour'}, {f'{el[3]} minutes'if el[3]>1 else f'{el[3]} minute'} and {f'{el[4]} seconds'if el[4]>1 else f'{el[4]} second'}'
            elif el[1]==0:
                es=f'{f'{el[0]} years'if el[0]>1 else f'{el[0]} year'}, {f'{el[2]} hours'if el[2]>1 else f'{el[2]} hour'}, {f'{el[3]} minutes'if el[3]>1 else f'{el[3]} minute'} and {f'{el[4]} seconds'if el[4]>1 else f'{el[4]} second'}'
            elif el[2]==0:
                es=f'{f'{el[0]} years'if el[0]>1 else f'{el[0]} year'},  {f'{el[1]} days'if el[1]>1 else f'{el[1]} day'}, {f'{el[3]} minutes'if el[3]>1 else f'{el[3]} minute'} and {f'{el[4]} seconds'if el[4]>1 else f'{el[4]} second'}'

            elif el[3]==0:
                es=f'{f'{el[0]} years'if el[0]>1 else f'{el[0]} year'}, {f'{el[1]} days'if el[1]>1 else f'{el[1]} day'}, {f'{el[2]} hours'if el[2]>1 else f'{el[2]} hour'} and {f'{el[4]} seconds'if el[4]>1 else f'{el[4]} second'}'

            elif el[4]==0:
                es=es=f'{f'{el[0]} years'if el[0]>1 else f'{el[0]} year'},{f'{el[1]} days'if el[1]>1 else f'{el[1]} day'}, {f'{el[2]} hours'if el[2]>1 else f'{el[2]} hour'} and {f'{el[3]} minutes'if el[3]>1 else f'{el[3]} minute'}'

        return es


    return format_output(list(map(int,rl)))
   


    
        
print(format_duration(11))

