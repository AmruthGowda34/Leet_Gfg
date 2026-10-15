class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def Add2Num(self,l1,l2):
        dummy=ListNode(0)
        current=dummy
        carry=0
        
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            
            total=x+y+carry
            carry=total//10
            digit=total%10
            
            current.next=ListNode(digit)
            current=current.next
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
        return dummy.next
        


def CreateList(values):
    dummy=ListNode(0)
    current=dummy
    
    for v in values:
        current.next=ListNode(v)
        current=current.next
    
    return dummy.next

def PrintLists(head):
    while head:
        print(head.val,end=" ")
        head=head.next
    
l1=CreateList([2,4,3])
l2=CreateList([5,6,4])
s=Solution()
res=s.Add2Num(l1,l2)

PrintLists(res)