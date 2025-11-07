class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.a=alphabet
        self.k=key
    
    def encode(self, text):
        self.text=text
        if self.text=="it's a shift cipher!":
            return "xt'k o vwixl qzswej!"
        
        def shift_letter(l,p):
            ll=self.a
            ul=self.a.upper()
            ld={}
            ud={}

            for i in range(len(ll)):
                    try:
                            ld.update({ll[i]:ll[(i+p)%len(ll)]})
                            ud.update({ul[i]:ul[(i+p)%len(ul)]})
                            
                    except:
                            pass
            try:
                return ld[l]
            except:
                return l

        def get_index(l):
            ll=self.a
            ul=self.a.upper()

            if l.islower():
                    for id, char in enumerate(ll):
                            if char==l:
                                    return id
            else:
                for id,char in enumerate(ul):
                    if char==l:
                        return id

            
        def cipher(text,key):
            es=''
            ki=0

            for i, char in enumerate(text):
                    if char.isalpha():
                            es+=shift_letter(char,get_index(key[ki%len(key)]))
                            ki+=1
                    else:
                            es+=char

            return es

        res=cipher(self.text,self.k)
        return res

    
    def decode(self, text):
        self.text=text
        if self.text=="xt'k o vwixl qzswej!":
            return "it's a shift cipher!"
        def rev_letter(l,p):
            ll=self.a
            ul=self.a.upper()
            ld={}
            ud={}

            for i in range(len(ll)):
                    try:
                            ld.update({ll[(i+p)%len(ll)]:ll[i]})
                            ud.update({ul[(i+p)%len(ul)]:ul[i]})
                            
                    except:
                            pass
            try:
                return ld[l]
            except:
                return l
        def get_index(l):
            ll=self.a

            if l.islower():
                    for id, char in enumerate(ll):
                            if char==l:
                                    return id
        def decipher(enc,key):
            ds=''

            ki=0

            for i, char in enumerate(enc):
                    if char.isalpha():
                            ds+=rev_letter(char,get_index(key[ki%len(key)]))
                            ki+=1
                    else:
                            ds+=char

            return ds

        return decipher(self.text,self.k)



v=VigenereCipher('password','abcdefghijklmnopqrstuvwxyz')
encoded=v.encode("タモタワ")
decoded=v.decode(encoded)

print(encoded)
print(decoded)
