# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        retype = ListNode(0)
        current, fixed = retype, 0
        while l1 or l2:
            count, sum = 0, 0
            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            sum = count + fixed
            fixed = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
        
        if fixed > 0:
            current.next = ListNode(fixed)

        return retype.next

if __name__ == '__main__':
    # a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    # b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    a = ListNode(1)
    b, b.next = ListNode(9), ListNode(9)
    result = Solution().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))