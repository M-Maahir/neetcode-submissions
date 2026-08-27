class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hsmp = {}

        for word in strs:
            count = [0]*26
            for l in word:
                count[ord(l) - ord('a')] += 1
            
            count =  tuple(count)

            if count not in hsmp:
                hsmp[count] = []
            hsmp[count].append(word)
        
        return list(hsmp.values())


        