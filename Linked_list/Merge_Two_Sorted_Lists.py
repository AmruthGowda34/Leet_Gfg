class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class SLL:
    def MergTwoSortedList(self,l1,l2):
        dummy=Node(0)
        curr=dummy
        
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
            
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        
        return dummy.next
    
def CreateList(values):
    dummy=Node(0)
    current=dummy
    
    for v in values:
        current.next=Node(v)
        current=current.next
    
    return dummy.next

def PrintLists(head):
    while head:
        print(head.val,end=" ")
        head=head.next
        
l1=CreateList([2,3,7])
l2=CreateList([1,6,7])
s1=SLL()
res=s1.MergTwoSortedList(l1,l2)
PrintLists(res)