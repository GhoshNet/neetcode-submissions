class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # groups = {}
        # # for word in strs:
        # #     key = "".join(sorted(word))
        # #     if key not in groups:
        # #         groups[key] = []
        # #     groups[key].append(word)

        # # return list(groups.values())

        # groups = {}

        # for word in strs:
        #     sw = tuple(sorted(word))
        #     # print(sw)
        #     if sw in groups:
        #         groups[sw].append(word)
        #     else:
        #         groups[sw] = [word]
        
        # finalList = groups.values()
        # finalList = list(finalList)
        # return finalList

        #Solved alone
        # group = {}
        # for word in strs:
        #     sorting = "".join(sorted(word))
        #     if sorting not in group:
        #         group[sorting] = [word]
        #     else:
        #         group[sorting].append(word)
        
        # return list(group.values())

        #Try 2
        group = {}
        for word in strs:
            sort = tuple(sorted(word))
            if sort not in group:
                group[sort] = []
            group[sort].append(word)
        
        result = list(group.values())
        return result