class SmartTrafficLight:
    def __init__(self, a, b):
        self.a = [] if a[0] == b[0] else sorted((a, b))
        
    def turngreen(self):
        if self.a:
            return self.a.pop()[1]
