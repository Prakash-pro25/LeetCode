class Solution(object):
    def mergeAlternately(self, word1, word2):

        max_len = max(len(word1), len(word2))
        word1 = word1.ljust(max_len)
        word2 = word2.ljust(max_len)
        """ words=" "
        i=0
        while i<max_len:

            words+=word1[i]+word2[i] 
            i+=1

        [print(i) for i in range(5)]     
        return words.replace(" ","") """
        words=""
        i=0
        while i < max_len: words += word1[i] + word2[i]; i += 1
        return words.replace(" ","")


c =Solution()

print(c.mergeAlternately('abc','pqr'))
print(c.mergeAlternately('ab','pqrs'))
print(c.mergeAlternately('abcd','pq'))