from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hsmp = defaultdict(list)

        for word in strs:
            count = [0]*26
            for i in range(len(word)):
                count[ord(word[i]) - ord("a")] += 1
            
            count = tuple(count)

            if count not in hsmp:
                hsmp[count] = []

            hsmp[count].append(word)
        
        return list(hsmp.values())

            