
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list. You may assume the two numbers
do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = '',''
        while True:
            try:
                s1 += str(l1.val)
                l1 = l1.next
            except:
                break

        while True:
            try:
                s2 += str(l2.val)
                l2 = l2.next
            except:
                break

        s = int(s1[::-1]) + int(s2[::-1])
        s = str(s)
        l = None
        i = 0
        # Creating a linked list
        while i < len(s):
            if l is None:
                l = ListNode(int(s[i]))
            else:
                node = ListNode(int(s[i]))
                node.next = l
                l = node
            i += 1

        return l

