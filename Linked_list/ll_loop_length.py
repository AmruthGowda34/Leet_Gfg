class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class SLL:
    def loop_len(self,head):
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        ind=1
        slow=slow.next
        while slow!=fast:
            ind+=1
            slow=slow.next
        return ind
        
s1=SLL()
values=[5,9,1,7,6,1,9,2,8]
head=Node(values[0])
current=head

for i in values[1:]:
    current.next=Node(i)
    current=current.next

temp=head
target=int(input("Enter index:"))
count=0

while count<target:
    temp=temp.next
    count+=1

current.next=temp
print(s1.loop_len(head))