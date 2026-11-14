class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        hcount=0
        count=0
        for i in sentences:
            count=len(i.split())
            hcount=max(count,hcount)
        return hcount
        