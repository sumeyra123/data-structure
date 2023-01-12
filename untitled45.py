# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:02:10 2023

@author: Sümeyra Nihal GELMEZ
"""

Suppose we have a basic class containing a single data field:
class ListNode :
def __init__( self, data ) :
self.data = data
We can create several instances of this class, each storing data of our choosing. In
the following example, we create three instances, each storing an integer value:
a = ListNode( 11 )
b = ListNode( 52 )
c = ListNode( 18 )
the result of which is the creation of three variables and three objects :
    
    class ListNode :
def __init__( self, data ) :
self.data = data
self.next = None

print( a.data )
print( a.next.data )
print( a.next.next.data )


Traversing a linked list.
 def traversal( head ):
 while curNode is not None :
 print curNode.data
 curNode = curNode.next
 
 Searching a linked list.
 def unorderedSearch( head, target ):
 curNode = head
 while curNode is not None and curNode.data != target :
 curNode= curNode.next
 return curNode is not None

Prepending a node to the linked list.
 # Given the head pointer, prepend an item to an unsorted linked list.
# Given the head pointer, prepend an item to an unsorted linked list.
 newNode = ListNode( item )
 newNode.next = head
 head = newNode
 
 
 
 
 Removing a node from a linked list.
 # Given the head reference, remove a target from a linked list.
 predNode = None
 curNode = head
 while curNode is not None and curNode.data != target :
 predNode = curNode
curNode = curNode.next

 if curNode is not None :
 if curNode is head :
 head = curNode.next
 else :
 predNode.next = curNode.next
 
 
 Searching a sorted linked list.
 def sortedSearch( head, target ) :
 curNode = head
while curNode is not None and curNode.data < target :
 if curNode.data == target :
 return True
 else :
 curNode = node.next
return False











