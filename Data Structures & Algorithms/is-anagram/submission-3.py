class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #Following solution is O(nLogn)
        # if len(s) != len(t): #O(n)
        #     return False
        # elif sorted(s) == sorted(t): #O(nlogn)
        #     return True
        # else:
        #     return False

        #Now in the following solution, we will use python dict 
        #to get the solution. 
        
        if len(s) != len(t):
            return False
        #Initialise Dict
        count = {}
        #Add characters in dict
        for char in s:
            count[char] = 1 + count.get(char, 0)
        for char in t:
            #Check if those characters are present or not ; 
            #And if present, then has it exceeded than string 1 as we are subtracting the counts;
            #If not in count or exceeds the count, then it's definitely not an anagram. 
            if char not in count or count[char] == 0:
                return False
            else:
                count[char] = count.get(char) - 1
        #If the algo has reached this step, it means it's an anagram
        return True