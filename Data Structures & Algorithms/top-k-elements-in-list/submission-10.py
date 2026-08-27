class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ls = [[] for i in range(len(nums)+1)]

        hsmp = {}

        for i in range(len(nums)):
            hsmp[nums[i]] = hsmp.get(nums[i], 0) + 1
        
        

        for key, freq in hsmp.items():
            ls[freq].append(key)
        
        res = []
        
        for i in range(len(ls)-1, -1, -1):
            for j in ls[i]:
                res.append(j)
                if len(res) == k:
                    return res


        