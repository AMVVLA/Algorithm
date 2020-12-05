# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Method 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        slow, fast = head, head
        stk = []

        while fast and fast.next:
            stk.append(slow.val)

            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next
        while (slow and len(stk)):
            if stk.pop() != slow.val:
                return False
            slow = slow.next
        return True

# Method 2
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next
        return s == s[::-1]