from collections import deque
class StackusingQueue:
    def __init__(self):
        self.queue=deque()
        
    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
    
    def disp(self):
        return self.queue
    
    def pop(self):
        if len(self.queue)==0:
            return "stack is empty"
        return self.queue.popleft()
    
    def peek(self):
        if len(self.queue)==0:
            return "Empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    

q1=StackusingQueue()
q1.push(100)
q1.push(200)
q1.push(300)
q1.push(400)
print(q1.disp())
q1.pop()
print(q1.is_empty())
print(q1.size())
print(q1.disp())
print(q1.peek())