class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hs = {}
        count = [[] for i in range(len(nums)+1)]
        res = []

        for i in nums:
            hs[i] = hs.get(i,0)+1


        for num, freq in hs.items():
            count[freq].append(num)

        
        for i in range(len(count)-1, -1, -1):
            for j in count[i]:
                res.append(j)
                if k == len(res):
                    return res


