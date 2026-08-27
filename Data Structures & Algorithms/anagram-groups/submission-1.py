from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dics = defaultdict(list)

        for word in strs:
            count = [0]*26

            for i in word:
                count[ord(i) - ord("a")] += 1

            key = tuple(count)
            dics[key].append(word)

        return list(dics.values())

            