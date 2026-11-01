class Solution(object):
    def longestCommonPrefix(self, strs):
        
        
        if not strs:
            return ""
            
        
        prefix = strs[0]
        
        
        for i in range(len(prefix)):
            for string in strs[1:]:
           
                if i >= len(string) or string[i] != prefix[i]:
                    return prefix[:i]
                    
        return prefix

c= Solution()

print(c.longestCommonPrefix(["flo","fl","fli"]))