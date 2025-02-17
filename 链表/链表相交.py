class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lenA = 0
        lenB = 0
        cur = headA

        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1

        curA = headA
        curB = headB
        if lenA > lenB:
            curA,curB = headB,headA
            lenA,lenB = lenB,lenA

        for _ in range(lenB-lenA):
            curB=curB.next

        while curA:
            if curA == curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None