# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr3 = res
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            sum = l1val + l2val + carry
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            digit = sum % 10
            carry = sum // 10
            curr3.next = ListNode(digit)
            curr3 = curr3.next
        return res.next

