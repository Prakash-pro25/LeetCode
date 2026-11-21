class Solution(object):
    def decodeMessage(self, key, message):

        al="abcdefghijklmnopqrstuvwxyz"
        index=0
        ht={}
        for i in key:
            if i in ht:
                continue
            elif i == " ":
                continue
            else:
                ht[i]=al[index]
                index+=1
        ht[" "]=" "


        ms=""
        for i in message:
            ms+=ht[i]
        return ms

c = Solution()

print(c.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
