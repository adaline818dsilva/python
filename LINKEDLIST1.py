class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
         self.head=None

    def add_data(self,data):
        newnode=Node(data) 
        if not self.head:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next!=None):
             temp=temp.next
            temp.next=newnode  
            
    def display(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


l=LinkedList()
l.add_data(20)
l.add_data(10)
l.add_data(25)
l.add_data(28)
