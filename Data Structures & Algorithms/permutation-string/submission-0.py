class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count = {}
        window = {}

        for char in s1:
            s1count[char] = s1count.get(char, 0) + 1

        left = 0
        right = 0
        for right in range(len(s2)):
            char = s2[right]
            window[char] = window.get(char, 0) + 1
            if (right - left + 1) > len(s1):
                leftChar = s2[left]
                window[leftChar] -= 1
                left += 1
                if window[leftChar] == 0:
                    del window[leftChar]
            
            if window == s1count:
                return True
        
        return False





