import string
def find_secret_message(paragraph):
    
    def n(s):
        for c in string.punctuation:
            if s.endswith(c):
            	s=s.replace(c,'')
        return s
    l2=[]
    for char in paragraph.split(" "):
        l2.append(n(char).lower())
    there=set()
    l3=[]
    
    for word in l2:
        
        if word in there:
            if word not in l3:
                l3.append(word)
        else:
            there.add(word)
    return ' '.join(l3)
    
print(find_secret_message("t-rex! think secret think: wants never chocolate sleeps, good. Pippi. a NOT! eats! never T-Rex Eats bad good! chocolate Sky: message secret: EATS is code Kills Think T-Rex have Chocolate, EATS!"))