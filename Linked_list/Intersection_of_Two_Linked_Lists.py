class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    

class Solution:
    def InterOf2LL(self,headA,headB):
        # lenA=0
        # lenB=0
        
        # a=headA
        # b=headB
        
        # while a:
        #     lenA+=1
        #     a=a.next
        
        # while b:
        #     lenB+=1
        #     b=b.next       
        
        # a=headA
        # b=headB
        
        # while lenA>lenB:
        #     a=a.next
        #     lenA-=1
        
        # while lenB>lenA:
        #     b=b.next
        #     lenB-=1
        
        # while a!=b:
        #     a=a.next
        #     b=b.next
        
        # return a
        
        a=headA
        b=headB
        
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        
        return a
