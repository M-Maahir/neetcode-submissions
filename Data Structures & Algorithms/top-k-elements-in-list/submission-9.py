class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hsmp = {}
        count = [[] for _ in range(len(nums)+1)]
        res = []

        for i in nums:
            hsmp[i] = 1 + hsmp.get(i, 0)
        
        for num, freq in hsmp.items():
            count[freq].append(num)

        for i in range(len(count)-1, 0, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
        