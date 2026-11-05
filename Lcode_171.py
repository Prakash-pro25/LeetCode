class Solution(object):
    def titleToNumber(self, columnTitle):
        s,j=0,0
        for i in columnTitle[::-1]:
            s+=(26**j)*(ord(i)-64)
            j+=1
        return s