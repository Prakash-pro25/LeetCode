class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1
        while l<=r:
            temp=s[l]
            s[l]=s[r]
            s[r]=temp
            l+=1
            r-=1 


c=Solution()
c.reverseString(s=["h","e","l","l","o"])


""" 
[1 , 2 , 3 , 4 , 5 ,6]
temp=1 r=6 l=r r=temp
[6,2,3,4,5,1]
 """
