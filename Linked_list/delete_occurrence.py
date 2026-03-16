class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None

class DLL:
    def del_occ(self,head,k):   
        if head.next is None and head.val==k:
            return None
        temp=head
        prev_n=None
        new_head=head
        while temp!=None:
            if temp.val==k:
                if prev_n!=None:
                    prev_n.next=temp.next
                if temp.next!=None:
                    temp.next.prev=prev_n
                if temp==new_head:
                    new_head=new_head.next
            else:
                prev_n=temp
            temp=temp.next
        return new_head
    def print_dll(self,new_head):
        while new_head:
            print(new_head.val,end=" ")
            new_head=new_head.next

s1=DLL()

values=[3,2,4,5,2]
head=Node(values[0])
current=head

for i in values[1:]:
    new_node=Node(i)
    current.next=new_node
    new_node.prev=current
    current=new_node
re=s1.del_occ(head,2)
s1.print_dll(re)