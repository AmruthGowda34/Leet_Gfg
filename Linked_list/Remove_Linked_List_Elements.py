class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def Remo_LL_Ele(self,head,n):
        dummy=Node(0)
        dummy.next=head
        prev=dummy
        temp=head
        
        while temp:
            if temp.val==n:
                prev.next=temp.next
            else:
                prev=temp
            
            temp=temp.next
        
        return dummy.next        
        
        
    def printList(slef,head):
        while head:
            print(head.val,end=" ")
            head=head.next
        

values=[1,2,6,3,4,5,6]
head=Node(values[0])
curr=head

for i in values[1:]:
    curr.next=Node(i)
    curr=curr.next

s1=Solution()
res=s1.Remo_LL_Ele(head,6)
s1.printList(res)