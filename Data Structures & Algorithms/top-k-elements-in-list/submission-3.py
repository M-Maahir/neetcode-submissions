class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hsmp = {}
        res = []

        ls = [[] for i in range(len(nums)+1)]

        for i in nums:
            hsmp[i] = hsmp.get(i, 0) + 1

        for num, freq in hsmp.items():
            ls[freq].append(num)

        
        for i in range(len(ls)-1,-1,-1):
            for j in ls[i]:
                res.append(j)
                if len(res)==k:
                    return res



        

        