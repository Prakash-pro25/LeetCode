class Solution(object):
    def findComplement(self, num):
        if num == 0:
            return 1
        # Create a mask of 1s matching the bit length of num
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
    

""" 
This function flips only the visible binary digits of a positive number (turning 1001 into 0110) without turning the result into a negative number.
Using num = 9 (which is 1001 in binary) as an example, here is how each line executes:

1. Handle the Zero Edge Case

python
if num == 0:
    return 1
Use code with caution.
• Why it is needed. In Python, (0).bit_length() returns 0. Without this check, the formula would create an empty mask of 0 and return 0 instead of flipping 0 to 1.

2. Count the Bits (num.bit_length())

python
num.bit_length()
Use code with caution.
• What it does. This built-in method counts how many bits are needed to write num in binary.
• With num = 9. The binary for 9 is 1001, which has 4 digits, so 9.bit_length() returns 4.

3. Build a Mask of All 1s

python
mask = (1 << num.bit_length()) - 1
Use code with caution.
This line creates a binary number made entirely of 1s that matches the length of num (for 9, we want 1111):
• Step A (1 << 4): Shifts the binary 1 four places to the left. This produces 10000 in binary (which is 16 in decimal).
• Step B (16 - 1): Subtracting 1 from 10000 borrows across all zeros, turning them into 1s. This gives 1111 in binary (which is 15 in decimal).

4. Flip the Bits with XOR (^)

python
return num ^ mask
Use code with caution.
The XOR (^) operator compares two bits and returns 1 only when they are different. Whenever you XOR any bit with 1, it flips:
• 1 ^ 1 becomes 0 (same bits)
• 0 ^ 1 becomes 1 (different bits)
Aligning 9 and the mask bit by bit shows the exact transformation:
text
  1001   (num = 9)
^ 1111   (mask = 15)
------
  0110   (result = 6)
Use code with caution.
Python returns 0110, which equals 6 in decimal.

"""