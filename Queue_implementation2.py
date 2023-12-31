# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:24:01 2023

@author: User
"""

class Node:
    def __init__(self,info):
        self.info = info
        self.link = None
        
class Queue:
    def __init__(self):
        self.head = None
        
    def print_Queue(self,head):
        while head != None:
            print(head.info)
            head = head.link
            
    def Enqueue(self,val):
        newNode = Node(val)
        lastNode = self.head
        while lastNode.link != None:
            lastNode = lastNode.link 
        lastNode.link = newNode
   
    def totalsize(self):
        c = 1
        current = self.head
        while(current):
            c += 1
            current = current.link 
        return c
    
    def Dequeue(self):
        self.head = self.head.link
           

first = Node(10)
second = Node(20)
third = Node(30)
L = Queue()

L.head = first
first.link = second
second.link = third
L.Enqueue(100)
L.Enqueue(200)
print('After Enqueue: ')
L.print_Queue(L.head)
L.Dequeue()
print('After Dequeue: ')
L.print_Queue(L.head)
        