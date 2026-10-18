class Solution:

    def encode(self, strs: List[str]) -> str:
    #     result = ""
    #     for word in strs:
    #         result = result + str(len(word))+"#"+word
    #     return result
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
        return result
        

    def decode(self, s: str) -> List[str]:
    #     result = []
    #     i = 0
    #     while i < len(s):
    #         # "4#word"
    #         j = i  
    #         while s[j] != "#":
    #             j += 1 
    #         lenght = int(s[i:j]) #4
    #         start = j+1 #2
    #         end = start + lenght 
    #         word = str(s[start:end])
    #         result.append(word)
    #         i = j+1+lenght
    #     return result

        #Try 2
        result = []
        i = 0
        while i < len(s):
            # 4#word
            j = i
            while s[j] != "#":
                j += 1
            start = j + 1
            # print(s[j-1]) #This won't work for double digits len
            # lenght = int(s[j-1])
            lenght = int(s[i:j])
            end = start + lenght
            word = str(s[start:end])
            result.append(word)
            i = j + 1 + lenght
        
        return result


