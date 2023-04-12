#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_lists(list1, list2, n):
    current1 = list1
    current2 = list2
    count = 1

    
    while current1 and count < n:
        current1 = current1.next
        count += 1
        if not current1:
            return list1
    next_node = current1.next
    while current2.next:
        current2 = current2.next
    current1.next = list2
    current2.next = next_node
    return list1
list1 = Node(1)
list1.next=Node(2)
list1.next.next=Node(3)
list1.next.next.next=Node(4)
list1.next.next.next.next=Node(5)

list2 = Node(9)
list2.next=Node(8)
list2.next.next=Node(11)

merged_list=merge_lists(list1, list2, 2)

while merged_list:
    print(str(merged_list.data)+"->",end=' ')
    merged_list=merged_list.next


# In[ ]:




