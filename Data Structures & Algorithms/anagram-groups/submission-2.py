from collections import defaultdict as dc

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = dc(list)

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            
            d[tuple(count)].append(word)

        return list(d.values())
        