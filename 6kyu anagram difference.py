def anagram_difference(w1, w2):
    def reml(w1,w2):
        es=''
        for c in w1:
            if c not in w2:
                es+=c
        return es
    g=set()
    r=''
    s1=len(w1)
    s2=len(w2)
    if s2>s1:
        for i in range(s2):
            for j in range(s1):
                if w2[i]==w1[j]:
                    g.add(w2[i])
            
    anagram=''.join(g)
    ans=len(reml(w1,anagram))+len(reml(w2,anagram))

    return ans

print(anagram_difference('codewars','hackerrank'))
