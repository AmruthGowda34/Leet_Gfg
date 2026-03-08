class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class SLL:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node=node(data)
        if self.head==None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node
            
    def traves(self):
        if self.head==None:
            print("SLL is empty!")
        else:
            current_node=self.head
            while current_node is not None:
                print(current_node.val,end=" ")
                current_node=current_node.next
            print()
            
    def insert_at(self,val,pos):
        new_node=node(val)
        if pos<0:
            print("Invalid position!")
            return 
        if pos==0:
            new_node.next=self.head
            self.head=new_node
            return 
        else:
            current=self.head
            prev=None
            count=0
            while current is not None and count<pos:
                prev=current
                current=current.next
                count+=1
            prev.next=new_node
            new_node.next=current
    def delete(self,val):
        if self.head is None:
            print("Empty SLL!")
            return
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                temp.next=None
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    del temp
                else:
                    print("element not in SLL")
                
s1=SLL()
s1.append(10)
s1.append(20)
s1.append(30)
s1.traves()
s1.insert_at(40,3)
s1.traves()
s1.delete(30)
s1.traves()
s1.delete(10)
s1.traves()