# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        leftNode =prev.next
        rightNode= leftNode
        for _ in range(right - left):
            rightNode = rightNode.next
        tail = rightNode.next

        rightNode.next = None
        prev.next = None

        cur= leftNode
        p = None
        while cur:
            next = cur.next
            cur.next = p
            p = cur
            cur = next

        prev.next = rightNode
        leftNode.next = tail


        return dummy.next