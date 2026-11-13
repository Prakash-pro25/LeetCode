class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        al="abcdefghijklmnopqrstuvwxyz"
        for i in al:
            if i not in sentence:
                return False
        return True