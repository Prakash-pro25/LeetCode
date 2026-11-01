class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        

        reversed_x = int(str(abs(x))[::-1]) * sign
        
        if reversed_x < -2147483648 or reversed_x > 2147483647:
            return 0
            
        return reversed_x
        