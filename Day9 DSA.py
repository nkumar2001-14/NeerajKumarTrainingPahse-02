#!/usr/bin/env python
# coding: utf-8

# In[5]:


#REVERSE SINGLE LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        ref=self.head
        while(ref is not None):
            print(ref.data)
            ref=ref.next
    
    
    
llist=LinkedList()
print("Given Linked List")
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.printlist()
llist.reverse()
print("Reverse Linked List")
llist.printlist()


# In[5]:


#DOUBLY LINKED LIST
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        c=0
        while temp is not None:
            temp=temp.next
            c+=1
        return c
    def insertatbeginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous==new_node
            self.head=new_node
    def insertatend(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertatbeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp
    def insertatposition(self,value,position):
        temp=self.head
        c=0
        while temp is not None:
            if c==position-1:
                break
            c+=1
            temp=temp.next
            if position==1:
                self.insertatbeginning(value)
            elif temp is None:
                print("There are less than {} -1 elements in the list ".format(position))
            elif temp.next is None:
                self.insertatend(value)
            else:
                new_node=Node(value)
                new_node.next=temp.next
                new_node.previous=temp
                temp.next.previous=new_node
                temp.next=new_node
    def deletefromlast(self):
        if self.isEmpty():
            print("The linked list is empty. Cannot delete elements")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None
    def deletefrombeginning(self):
        if self.isEmpty():
            print("The linked list is empty. Cannot delete elements")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous=None
    def deletefromposition(self,position):
        if self.isEmpty():
            print("The linked list is empty. Cannot delete elements")
        elif position==1:
            self.deletefrombeginning()
        else:
            temp=self.head
            c=1
            while temp is not None:
                if c==position:
                    break
                temp=temp.next
                c+=1
            if temp is None:
                print("There are less than {} elements in the list . Cannot delete elements".format(position))
            elif temp.next is None:
                self.deletefromlast()
            temp.previous.next=temp.next
            temp.next.previous=temp.previous
            temp.previous=None
    
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=' ')
            temp=temp.next
x=DoublyLinkedList()
#print(x.isEmpty())
x.insertatend(5)
x.insertatend(15)
x.insertatend(25)
x.insertatend(35)
x.insertatend(45)
x.printlist()
x.insertatbeginning(50)
print("After insertion at beginning")
x.printlist()
print("No of nodes",x.length())
print("Insert at position 2 number 8")
x.insertatposition(8,2)
x.printlist()
print("After Deleting from last")
x.deletefromlast()
x.printlist()
print("After Deleting from beginning")
x.deletefrombeginning()
x.printlist()
print("after deleting at position 2 number 8")
x.deletefromposition(3)
x.printlist()


# In[8]:


#EVALUATE POSTFIX EXPRESSION
#231*+9-   -> 3*1   ->23+9-      ->  59-      ->   -4 OR 4
class Evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if self.top ==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
    def evaluatepostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2 + i +val1)))
        return int(self.pop())
if __name__ =='__main__':
    exp="231*+9-"
    obj=Evaluate(len(exp))
    print("Postfix Evaluation: %d"%(obj.evaluatepostfix(exp)))

