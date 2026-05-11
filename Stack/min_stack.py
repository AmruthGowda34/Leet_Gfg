class Solution:
    def __init__(self):
        self.items=[]
    
    def push(self,val):
        if len(self.items)==0:
            self.items.append([val,val])
        else:
            mini=min(self.items[-1][1],val)
            self.items.append([val,mini])
    
    def pop(self):
        return self.items.pop()
    
    def get_min(self):
        if len(self.items)==0:
            return "It is empty"
        return self.items[-1][1]
    
    def top(self):
        if len(self.items)==0:
            return "It is empty"
        return self.items[-1][0]
    
    def display(self):
        return self.items

s1=Solution()
s1.push(3)
s1.push(4)
s1.push(5)
s1.push(49)
print(s1.get_min())
print(s1.pop())
print(s1.get_min())
print(s1.display())