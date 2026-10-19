class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            start = j + 1
            lenght = int(s[i:j])
            end = start + lenght
            word = s[start:end]
            result.append(word)
            i = j + 1 + lenght
        return result

