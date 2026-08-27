from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dicts = defaultdict(list)

        for word in strs:
            count = [0]*26
            for l in word:
                count[ord(l) - ord("a")] += 1

            dicts[tuple(count)].append(word)

        return list(dicts.values())
            
        