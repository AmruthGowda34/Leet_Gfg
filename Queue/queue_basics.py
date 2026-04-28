class Queue:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return len(self.items)==0
    
    def en_queue(self,item):
        self.items.append(item)
    
    def de_queue(self):
        if len(self.items)==0:
            return "queue is empty can't delete"
        x=self.items.pop(0)
        return x
    
    def front(self):
        if len(self.items)==0:
            return "Queue is empty can't peek"
        return self.items[0]
    
    def rear(self):
        if len(self.items)==0:
            return "Queue is empty can't read"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items

q=Queue()

print(q.is_empty())
q.en_queue(67)
q.en_queue(68)
q.en_queue(69)
print(q.display())
print(q.rear())
print(q.de_queue())
print(q.is_empty())
print(q.display())
print(q.size())