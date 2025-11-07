class Dictionary():
    
    def __init__(self):
        # Your code
        global ed
        ed={}
    def newentry(self, word, definition):
        # Your code
        ed.update({word:definition})
        
    def look(self, key):
        # your code
        return ed[key]
        


d=Dictionary()
d.newentry('a','b')
print(d.look('a'))
