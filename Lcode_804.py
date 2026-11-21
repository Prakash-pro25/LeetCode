class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code_dict = {
            'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.',    'f': '..-.', 'g': '--.',  'h': '....',
            'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..',
            'm': '--',   'n': '-.',   'o': '---',  'p': '.--.',
            'q': '--.-', 'r': '.-.',  's': '...',  't': '-',
            'u': '..-',  'v': '...-', 'w': '.--',  'x': '-..-',
            'y': '-.--', 'z': '--..'
        }
        ht={}
        for word in words:
            encoded = "".join(morse_code_dict[char] for char in word)
            ht[encoded]=0
        
        return len(ht)
        