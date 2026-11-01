class Solution(object):
    def addStrings(self, num1, num2):

        """ 48 to 57 """
        n=max(len(num1),len(num2))
        a=[0]*(n-len(num1))
        b=[0]*(n-len(num2))
        i=0
        while i<n:  
              if i < len(num1):
                 a.append(ord(num1[i])-48)
              if i <len(num2): 
                 b.append(ord(num2[i])-48)
              i+=1   
        
        result=[]
        c=0

        for i in range(len(a)-1,-1,-1):
            if i==0:
                result.append(str({a[i]+b[i]+c}))
                break
            s=(a[i]+b[i])%10
            result.append(str({s+c}))
            c=(a[i]+b[i])//10
        
        return "".join(result[::-1])

    def added(self, num1, num2):
        num1=num1[::-1]
        num2=num2[::-1]
        a=sum((ord(num1[i])-48)*(10**i) for i in range(len(num1)))
        b=sum((ord(num2[i])-48)*(10**i) for i in range(len(num2)))

        return str(a+b)
    
    def added2(self, num1, num2):
            num1=num1[::-1]
            num2=num2[::-1]

            s1=0
            s2=0
            i=0    
            while i<max(len(num1),len(num2)):

                if i < len(num1):
                    s1+=(ord(num1[i])-48)*(10**i)
                if i < len(num2):
                    s2+=(ord(num2[i])-48)*(10**i)
                i+=1    
            
            return str(s1+s2)
    def added3(self, num1, num2):
        return eval(num2+"+"+num1)

    def added4(self, num1, num2):
        return str(int(num1)+int(num2))

    def added5(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

            a = ord(num1[i]) - 48 if i >= 0 else 0
            b = ord(num2[j]) - 48 if j >= 0 else 0

            total = a + b + carry

            result.append(str(total % 10))
            carry = total // 10

            i -= 1
            j -= 1

        return ''.join(result[::-1])

c=Solution()

print(c.addStrings("11","123"))
print(c.added("11","123"))
print(c.added2("11","123"))
print(c.added3("11","123"))



    

