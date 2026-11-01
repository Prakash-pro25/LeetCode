class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        i=0
        while i < len(word):
            if word[i]==ch:
                break
            i+=1
           

        return word[i::-1]+word[i+1::]   
         


c =Solution()

print(c.reversePrefix("abcdefd","d"))
    