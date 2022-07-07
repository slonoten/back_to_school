"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        im_head = ListNode()
        res_tail = im_head
        src_heads = lists
        for j in [i for i in range(len(src_heads) - 1, -1, -1) if not src_heads[i]]:
            del src_heads[j]
        while src_heads:
            min_value = 10001 # Constraint
            for i in range(len(src_heads)):
                if src_heads[i].val <= min_value:
                    min_value = src_heads[i].val 
                    next_head_idx = i
            while min_value == src_heads[next_head_idx].val:
                node_to_move = src_heads[next_head_idx]
                res_tail.next = node_to_move
                res_tail = node_to_move
                if node_to_move.next:
                    src_heads[next_head_idx] = node_to_move.next
                else:
                    del src_heads[next_head_idx]
                    break
        return im_head.next


class SolutionX:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        im_head = ListNode()
        res_tail = im_head
        numbers = []
        for head in lists:
            while head:
                numbers.append(head.val)
                head = head.next
        numbers.sort()
        for n in numbers:
            res_tail.next = ListNode(n)
            res_tail = res_tail.next
        return im_head.next


class SolutionXX:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head = None
        numbers = []
        for head in lists:
            while head:
                numbers.append(head.val)
                head = head.next
        numbers.sort(reverse=True)
        for n in numbers:
            res_head = ListNode(n, res_head)
        return res_head


class Solution99PersentOfShameFast:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_head = None
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next
        nodes.sort(key=lambda n: n.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0] if nodes else None



class SolutionRealMerge:
    """2.5 times slower then team sort based 99% solution, but it's real merge )"""
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        src_heads = lists
        for j in [i for i in range(len(src_heads) - 1, -1, -1) if not src_heads[i]]:
            del src_heads[j]
        while len(src_heads) > 1:
            for i in range(len(src_heads) - 1, 0, -2):
                h1 = src_heads[i - 1]
                h2 = src_heads[i]
                im_head = ListNode()
                res_tail = im_head
                while True:
                    if h1.val < h2.val:
                        res_tail.next = h1
                        res_tail = h1
                        h1 = h1.next
                        if not h1:
                            res_tail.next = h2
                            break
                    else:
                        res_tail.next = h2
                        res_tail = h2
                        h2 = h2.next
                        if not h2:
                            res_tail.next = h1
                            break
                src_heads[i - 1] = im_head.next
                del src_heads[i]
        return src_heads[0] if src_heads else None