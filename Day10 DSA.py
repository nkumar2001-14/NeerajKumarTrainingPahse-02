#!/usr/bin/env python
# coding: utf-8

# In[3]:


def LinearSearch(array,n,x):
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
array=[2,4,0,1,9]
x=1
n=len(array)
result=LinearSearch(array,n,x)
if(result==-1):
    print("Element Not found")
else:
    print("Element found at index",result)


# In[7]:


def BinarySearch(array,x,low,high):
    while low<=high:
        mid=low+(high - low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=5
result=BinarySearch(array,x,0,len(array)-1)
if result!=-1:
    print("Element is present at index "+str(result))
else:
    print("Element not forund")


# In[16]:


class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->",end=' ')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+"->",end=' ')
def preorder(root):
    if root:
        print(str(root.val)+ "->",end=' ')
        preorder(root.left)
        preorder(root.right)
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
print("Inorder Traversal")
inorder(root)
print("\nPreorder Traversal")
preorder(root)
print("\nPostorder Traversal")
postorder(root)


# In[3]:


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->",end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minvaluenode(Node):
    current=Node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):#8000,4/ 3000,4/ 6000,4/ 4000,4
    if root is None:
        return root
    if key<root.key:#4<8/ 4<3 F/ 4<6
        root.left=deleteNode(root.left,key)#3000,4/ 4000,4
    elif(key>root.key):#4>3
        root.right=deleteNode(root.right,key)#6000,4
    else:
        if root.left is None:
            temp=root.right#temp=none
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minvaluenode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root

root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("Inorder Traversal:",end=' ')
inorder(root)
print("\nDelete 4")
root=deleteNode(root,4)
print("Inorder Traversal:",end=' ')
inorder(root)
print("\nDelete 6")
root=deleteNode(root,6)
print("Inorder Traversal:",end=' ')
inorder(root)
print("\nDelete 8")
root=deleteNode(root,8)
print("Inorder Traversal:",end=' ')
inorder(root)

