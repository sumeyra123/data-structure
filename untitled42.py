# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 20:55:48 2023

@author: Sümeyra Nihal GELMEZ
"""

 In Python, a
target item can be found in a sequence using the in operator:
    if key in theArray :
print( "The key is in the array." )
else :
print( "The key is not in the array." )


Implementation of the linear search on an unsorted sequence.
 def linearSearch( theValues, target ) :
 n = len( theValues )
 for i in range( n ) :
# If the target is in the ith element, return True
 if theValues[i] == target
return True

 return False # If not found, return False.

Implementation of the linear search on a sorted sequence.
 def sortedLinearSearch( theValues, item ) :
 n = len( theValues )
for i in range( n ) :
# If the target is found in the ith element, return True if theValues[i] == item :
return True
# If target is larger than the ith element, it's not in the sequence.
elif theValues[i] > item :
 return False

 return False # The item is not in the sequence.

Searching for the smallest value in an unsorted sequence.
 def findSmallest( theValues ):
 n = len( theValues )
# Assume the first item is the smallest value.4 smallest = theValues[0]
 # Determine if any other item in the sequence is smaller.
 for i in range( 1, n ) :
 if theList[i] < smallest :
 smallest = theValues[i]

return smallest # Return the smallest found.

Sorting is the process of arranging or ordering a collection of items such that each
item and its successor satisfy a prescribed relationship.


Implementation of the bubble sort algorithm.
 # Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ):
 n = len( theSeq )
 # Perform n-1 bubble operations on the sequence
 for i in range( n - 1 ) :
 # Bubble the largest item to the end.
for j in range( i + n - 1 ) :
 if theSeq[j] > theSeq[j + 1] : # swap the j and j+1 items.
 tmp = theSeq[j]
 theSeq[j] = theSeq[j + 1]
 theSeq[j + 1] = tmp
 
 



