class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        hsmp = {}

        for word in strs:

            ls = [0]*26

            for letters in word:
                ls[ord(letters) - ord('a')] += 1

            ls = tuple(ls)

            if ls not in hsmp:
                hsmp[ls] = []
            
            hsmp[ls].append(word)
        
        return list(hsmp.values())



        