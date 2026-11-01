class Solution(object):
    def defangIPaddr(self, address):

        return address.replace(".","[.]")

c=Solution()

print(c.defangIPaddr("1.1.1.1"))