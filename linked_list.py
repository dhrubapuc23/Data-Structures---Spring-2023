# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:57:26 2023

@author: User
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traverse(self,head):
        while head != None:
            print(head.data)
            head = head.next
        
        
first = Node(10)
second = Node(20)
third = Node(30)
newNode = Node(40)
endNode = Node(50)
midNode = Node(60)

L = LinkedList()
L.head = first
first.next = second
second.next = third
newNode.next = L.head
L.head = newNode
#End node
third.next = endNode


#insert at mid
temp = L.head 
while temp != None:
    if temp.data == 20:
        break 
    else:
        temp = temp.next

midNode.next = temp.next
temp.next = midNode

L.traverse(L.head)








