#!/usr/bin/env python
# coding: utf-8

# In[5]:


#STACK OPERATIONS
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    def push(self,data):
        if(self.is_full()):
            print("The Stack Is full !!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty !!!")
        else:
            data=self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The Stack is empty !!!")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size
ball_stack=Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
print("The Element Deleted",ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())


# In[14]:


# QUEUE OPERATIONS
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("The Queue Is full !!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty !!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
queue1=Queue(4)
print("Is it full",queue1.is_full())
print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
print("Element Deleted",queue1.dequeue())
queue1.display()


# In[18]:


l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay','None','le','n']
new=[]
for i in range(len(l1)):
    if l1[i] is None:
        new.append(l2[-(i+1)])
    else:
        new.append(l1[i])
new_str=' '.join([word for word in reversed(new)])
print(new_str)


# In[17]:


def num(queue):
    div_q=[]
    for num in queue:
        if all(num%i==0 for i in range(1,11)):
            div_q.append(num)
    return div_q
in_queue=[13983,10080,7113,2520,2500]
out_queue=num(in_queue)
print(out_queue)


# In[21]:


def merged_queue(queue1,queue2):
    len1=len(queue1)
    len2=len(queue2)
    merged_queue=[]
    for i in range(min(len1,len2)):
        merged_queue.append(queue1[i])
        merged_queue.append(queue2[i])
    if len1>len2:
        merged_queue+=queue1[len2:]
    elif len2>len1:
        merged_queue+=queue2[len1:]
    return merged_queue
queue1=[3,6,8]
queue2=['b','y','u','t','r','o']
merged_queue=merged_queue(queue1,queue2)
print(merged_queue)


# In[22]:


def check(num_queue):
    sol_queue1=Queue(5)
    while(not num_queue.is_empty()):
        status=0
        element=num_queue.dequeue()
        for i in range(1,11):
            if element%i !=0:
                status=1
                break
        if status==0:
            sol_queue1.enqueue(element)
    return sol_queue1


# In[24]:


class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

            
list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.listprint()


# In[ ]:




