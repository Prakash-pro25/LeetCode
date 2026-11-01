# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n=max(len(l1),len(l2))
        l1=l1.extend([0]*(n-len(l1)))
        l2=l2.extend([0]*(n-len(l2)))
        c=0
        ans=[]
        for i in range(n):
            s=(l1[i]+l2[i]+c)//10
            ans.append(s)
            c=(l1[i]+l2[i]+c)%10

        return ans

c=Solution()

print(c.addTwoNumbers([1,2,3],[1,2,3]))







        