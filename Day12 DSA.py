#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])
data=[20,12,10,15,2]
size=len(data)
selectionsort(data,size)
print('Sorted Array in Ascending Order:')
print(data)


# In[3]:


class Employee:
    def __init__(self, name, basic_salary, qualification):
        self.name = name
        self.basic_salary = basic_salary
        self.qualification = qualification
   
    def validate_basic_salary(self):
        if self.basic_salary > 3000:
            return True
        else:
            return False
   
    def validate_qualification(self):
        if self.qualification == "Bachelors" or self.qualification == "Masters":
            return True
        else:
            return False

class Graduate(Employee):
    def __init__(self, name, basic_salary, qualification, job_band, cgpa):
        super().__init__(name, basic_salary, qualification)
        self.job_band = job_band
        self.cgpa = cgpa
   
    def validate_job_band(self):
        if self.job_band == "A" or self.job_band == "B" or self.job_band == "C":
            return True
        else:
            return False
   
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
           
            if 4 <= self.cgpa <= 4.25:
                tpi = 1000
            elif 4.26 <= self.cgpa <= 4.5:
                tpi = 1700
            elif 4.51 <= self.cgpa <= 4.75:
                tpi = 3200
            elif 4.76 <= self.cgpa <= 5:
                tpi = 5000
           
            if self.job_band == "A":
                incentive = 0.04 * self.basic_salary
            elif self.job_band == "B":
                incentive = 0.06 * self.basic_salary
            elif self.job_band == "C":
                incentive = 0.1 * self.basic_salary
           
            gross_salary = self.basic_salary + pf + tpi + incentive
            return gross_salary
        else:
            return -1

class Lateral(Employee):
    def __init__(self, name, basic_salary, qualification, job_band, skill_set):
        super().__init__(name, basic_salary, qualification)
        self.job_band = job_band
        self.skill_set = skill_set
   
    def validate_job_band(self):
        if self.job_band == "D" or self.job_band == "E" or self.job_band == "F":
            return True
        else:
            return False
   
    def calculate_gross_salary(self):
        if self.validate_basic_salary() and self.validate_qualification() and self.validate_job_band():
            pf = 0.12 * self.basic_salary
           
            if self.skill_set == "AGP":
                sme_bonus = 6500
            elif self.skill_set == "AGPT":
                sme_bonus = 8200
            elif self.skill_set == "AGDEV":
                sme_bonus = 11500
           
            if self.job_band == "D":
                incentive = 0.13 * self.basic_salary
            elif self.job_band == "E":
                incentive = 0.16 * self.basic_salary
            elif self.job_band == "F":
                incentive = 0.2 * self.basic_salary
           
            gross_salary = self.basic_salary + pf + sme_bonus + incentive
            return gross_salary
        else:
            return -1

g1 = Graduate("Neeraj Kumar", 400000, "Masters", "A", 8.71)
print("Graduate Details:")
print("Name-", g1.name)
print("Basic Salary-", g1.basic_salary)
print("Specializations-", g1.qualification)
print("Job Brand-", g1.job_band)
print("CGPA-",g1.cgpa)


# In[4]:


'''The owner of a BakeHouse wants to keep track of the tables
that are occupied in his cafe. Assume that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is 
occupied, it must be added to the occupied_table_list and when a customer leaves, the corresponding table must be removed 
from the list.
BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class.
Represent occupied_table_list using an appropriate data structure.

Note: Table numbers should be maintained in ascending order in the occupied_table_list.
Tables should be allocated and de-allocated as mentioned in the example below:

Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, he should be allocated table 5 
and the table list should be accordingly updated. If now customer at table 2 leaves, table list should be accordingly updated
and the next new customer should be allocated table 2 as it is the first free table.


Implement the allocation logic in allocate_table() method and de-allocation logic in deallocate_table() method.
-------------------------------------------------------
10.Write a python program to reverse a linked list containing integer data.
Use the LinkedList class and methods in it to implement the above program.
'''
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []
   
    def get_occupied_table_list(self):
        return self.occupied_table_list
   
    def allocate_table(self):
        if not self.occupied_table_list:
            self.occupied_table_list.append(1)
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list)-1:
                    if self.occupied_table_list[i] != 10:
                        self.occupied_table_list.append(self.occupied_table_list[i]+1)
                        break
                elif self.occupied_table_list[i+1] - self.occupied_table_list[i] > 1:
                    self.occupied_table_list.insert(i+1, self.occupied_table_list[i]+1)
                    break
   
    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
   
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
   
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
   
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
           
linked_list=LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()


# In[5]:


def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low, high):
        if array[j]<=pivot:
            i=i+1
            (array[i], array[j])=(array[j], array[i])
    (array[i + 1], array[high])=(array[high],array[i+1])
    return i+1
#function to perform quicksort
def quickSort(array, low, high):
    if low<high:
        pi=partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
data=[8,7,6,1,0,9,2]
print("Unsorted Array")
print(data)
size=len(data)
quickSort(data, 0, size-1)
print('Sorted Array in Ascending Order:')
print(data)


# In[7]:


'''Write a python program that accepts a text and displays a
string which contains the word with the largest frequency
 in the text and the
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a
single space between the words.
Perform case insensitive string comparisons wherever
necessary.'''
text = input("Enter the text: ")
text = text.lower()
words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

max_freq = 0
max_word = ""

for word in freq:
    if freq[word] > max_freq:
        max_freq = freq[word]
        max_word = word
    elif freq[word] == max_freq:
        if len(word) > len(max_word):
            max_word = word
print(max_word, max_freq)


# In[8]:


'''A teacher is conducting a camp for a group of five children.
 Based on their performance and behavior during the camp, the
 teacher rewards them with chocolates.
Write a Python function to Find the total number of chocolates
received by all the children put together.
Assume that each child is identified by an id and it is stored
 in a tuple and the number of chocolates given to each child
 is stored in a list.
The teacher also rewards a child with few extra chocolates
for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error
message "Extra chocolates is less than 1", should be
displayed.
If the given child Id is invalid, an error message
"Child id is invalid" should be displayed. Otherwise,
 the extra chocolates
provided for the child must be added to his/her existing
number of chocolates and display the list containing the
 total number of chocolates received by each child.
 child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

functions

calculate_total_chocolates()

reward_child(child_id_rewarded,extra_chocolates)
 '''

child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    total_chocolates = sum(chocolates_received)
    return total_chocolates

def reward_child(child_id_rewarded, extra_chocolates):
    if extra_chocolates < 1:
        print("Error: Extra chocolates is less than 1")
        return
   
    if child_id_rewarded not in child_id:
        print("Error: Child ID is invalid")
        return
   
    child_index = child_id.index(child_id_rewarded)
    chocolates_received[child_index] += extra_chocolates
    print(chocolates_received)
   
total_chocolates = calculate_total_chocolates()
print("Total number of chocolates received:", total_chocolates)
reward_child(20, 3) 


# In[9]:


'''Write a python program to help an airport manager to generate
 few statistics based on the ticket details available for a
day.
Go through the below program and complete it based on the comments mentioned in it.
Note: Perform case sensitive string comparisons wherever necessary.



#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
#find_passengers_per_flight()
print(sort_passenger_list())'''

ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name):
    passengers = []
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        if flight_no.startswith(airline_name):
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_destination(destination):
    passengers = []
    for ticket in ticket_list:
        if ticket.split(":")[2] == destination:
            passengers.append(ticket.split(":")[-1])
    return passengers

def find_passengers_per_flight():
    passengers_per_flight = {}
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        if flight_no not in passengers_per_flight:
            passengers_per_flight[flight_no] = 1
        else:
            passengers_per_flight[flight_no] += 1
    for flight_no, count in passengers_per_flight.items():
        print(f"Flight {flight_no} has {count} passengers.")

def sort_passenger_list():
    return sorted(ticket.split(":")[-1] for ticket in ticket_list)

print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
find_passengers_per_flight()
print(sort_passenger_list())


# In[ ]:




