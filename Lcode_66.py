class Solution(object):
    def plusOne(self, digits):
        digits=digits[::-1]
        c=1
        a=[]
        for i in range(len(digits)+1):
            if i<len(digits):
                s=digits[i]+c
                a.append(s%10)
                c=s//10
            elif c!=0:
                a.append(c)
                break    
        return a[::-1]

c=Solution()

print(c.plusOne(digits = [1,2,3]))
print(c.plusOne(digits = [9,9,9]))

            
            
