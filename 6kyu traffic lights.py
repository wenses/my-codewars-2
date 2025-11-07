class SmartTrafficLight:
    def __init__(self, st1, st2):
        
        self.st1=st1
        self.st2=st2

    
    
        
    def turngreen(self):
        if self.st1 is None and self.st2 is None:
            result=None
        elif self.st1 is None:
            result=self.st2[1]
            self.st2=None
        elif self.st2 is None:
            result=self.st1[1]
            self.st1=None
            return result
        
        try:
            if self.st1[0]>self.st2[0]:
                result=self.st1[1]
                self.st1=None
            elif self.st1[0]<self.st2[0]:
                result=self.st2[1]
                self.st2=None
            return result
        except:
            return None
            
       


t = SmartTrafficLight([71, '27th ave'], [72, '3rd st'])

print(t.turngreen())
print(t.turngreen())
print(t.turngreen())




