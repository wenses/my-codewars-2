def inside_out(st):
    def si(st):
        s=len(st)
        if s%2==0:
            w1=st[0:int(s/2)]
            w2=st[int(s/2):s]
            res=w1[::-1]+w2[::-1]
        else:
            m=st[int(s/2)]
            w1=st[0:int(s/2)]
            w2=st[int(s/2)+1:s]
            res=w1[::-1]+m+w2[::-1]
        return res
    el=[]
    es=''
    for word in st.split():
        try:
            el.append(si(word))
            es+=si(word)
        except:
            el.append(word)
            es+=word
        
    return ' '.join(e


print(inside_out('man i need a taxi up to ubud'))
