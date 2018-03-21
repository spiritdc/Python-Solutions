class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists( l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists( l1, l2.next)
            return l2

l1 = ListNode(1)
l11 = ListNode(2)
l111 = ListNode(5)
l11.next = l111
l1.next = l11

l2 = ListNode(1)
l22 = ListNode(3)
l222 = ListNode(4)
l22.next = l222
l2.next = l22
            
ret = Solution().mergeTwoLists(l1, l2)

while ret != None:
    print(ret.val)
    ret = ret.next