import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for list in lists:
            print(pq)
            node = list
            while node:
                heapq.heappush(pq, node.val)
                node = node.next

        first = None
        last = None

        while pq:
            if not first:
                first = ListNode(heapq.heappop(pq))
                last = first
            elif last:
                last.next = ListNode(heapq.heappop(pq))
                last = last.next

        return first

    def getList(self, node: Optional[ListNode]):
        resp = []
        while node:
            resp.append(node.val)
            node = node.next

        return resp


def test_removeKdigits():
    node1 = ListNode(1, ListNode(4, ListNode(5)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    node3 = ListNode(2, ListNode(6))
    assert Solution().getList(Solution().mergeKLists([node1, node2, node3])) == [
        1,
        1,
        2,
        3,
        4,
        4,
        5,
        6,
    ]

    assert Solution().getList(Solution().mergeKLists([])) == []
    assert Solution().getList(Solution().mergeKLists([[]])) == []
