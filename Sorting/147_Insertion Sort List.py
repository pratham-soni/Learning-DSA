"""
Docstring for Sorting.147_Insertion Sort List

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
"""

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr=[4,2,3,1]
def createLL(arr) -> Optional[ListNode]:
    if(len(arr)==0):
        return
    head = curr = ListNode(arr[0])
    i=1
    while i < len(arr):
        curr.next = ListNode(arr[i])
        curr = curr.next
        i+=1
    curr.next = None
    return head

# Method to print the linked list
def print_list(head):
    current = head  # Start from the head node
    while current:
        print(current.val, end=" -> ")  # Print the data of the current node
        current = current.next  # Move to the next node
    print("None") # Indicate the end of the list

linkedList = createLL(arr)
print("original Linked List : ", end="")
print_list(linkedList)

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return
        dummyHead = ListNode(0,head)
        curr = head.next
        prev = head
        while curr:
            # print_list(dummyHead)
            # print("prev : ",end="")
            # print_list(prev)
            # print("curr : ",end="")
            # print_list(curr)

            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            temp = dummyHead
            while curr.val > temp.next.val:
                temp = temp.next
            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next
        # print_list(dummyHead)
        return dummyHead.next

sol = Solution()
# print("after insertion sort : ", end="")
print_list(sol.insertionSortList(linkedList))