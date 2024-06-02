# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        while i < len(s):
            if l is None:
                l = ListNode(int(s[i]))
            else:
                node = ListNode(int(s[i]))
                node.next = l
                l = node
            i += 1
            
        return l
        
