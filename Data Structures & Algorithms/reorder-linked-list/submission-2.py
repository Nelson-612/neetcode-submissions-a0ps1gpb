class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        cur = slow.next
        slow.next = None  # cut the list in half

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        # Step 3: merge two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2