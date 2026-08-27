class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        hsmp = {}

        count = [[] for _ in range(len(nums)+1)]

        for i in nums:
            hsmp[i] = hsmp.get(i, 0) + 1

        for num, frq in hsmp.items():
            count[frq].append(num)

        for i in range(len(count)-1, -1, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res
