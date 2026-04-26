class stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items)==0:
            return "stack is empty."
        x=self.items.pop()
        return x
    
    def top(self):
        if len(self.items)==0:
            return "cannot top because it is empty."
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
s=stack()
print(s.is_empty())
s.push(70)
s.push(71)
s.push(72)
print(s.display())
s.pop()
print(s.display())
print(s.size())
s.push(49)
print(s.top())