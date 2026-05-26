class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        mostFreq = 0
        longest = 0
        for right in range(len(s)):
            #Counting and adding the Character in the dict
            count[s[right]] = count.get(s[right], 0) + 1
            
            if count[s[right]] > mostFreq:
                mostFreq = count[s[right]]
            
            window_len = right - left + 1
            replacementNeeded = window_len - mostFreq
            while replacementNeeded > k:
                leftChar = s[left]
                count[leftChar] -= 1
                left += 1
                window_len = right - left + 1
                replacementNeeded = window_len - mostFreq

            if window_len > longest:
                longest = window_len
        
        return longest