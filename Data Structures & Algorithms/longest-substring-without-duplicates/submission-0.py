class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #This is a sliding window problem. We will start pointers from left (- both right and left pointers).
        # And then start slinding the right pointer until we encounter a duplicate word. Then update the left pointer and then continue again.

        hashmap = set()
        left = 0
        right = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in hashmap:
                hashmap.remove(s[left])
                left += 1
            hashmap.add(s[right])
            right += 1
            longest = max(longest, (right - left))

        return longest