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
    def delete1(self,a):
        if(self.head==None):
            print("Delete not possible")
            return
        elif(a==1):
            temp=self.head
            self.head=temp.next
        else:
            prev=None
            current=self.head
            for i in range
            prev


l = LinkedList()
l.add_data(20)
l.add_data(25)
l.add_data(28)
l.display() 
l.delete1()                                                                                            
