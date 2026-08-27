class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hsmp = {}
        
        for word in strs:
            count = [0]*26
            for l in word:
                count[ord(l) - ord('a')] += 1
            
            w = tuple(count)

            if w not in hsmp:
                hsmp[w] = []
            hsmp[w].append(word)
        
        return list(hsmp.values())


        