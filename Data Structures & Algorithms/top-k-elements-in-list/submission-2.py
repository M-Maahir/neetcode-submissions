class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hsmp = {}

        res = [[] for i in range(len(nums)+1)]

        ans = []

        for num in nums:
            hsmp[num] = hsmp.get(num, 0) + 1

        for nums, freq in hsmp.items():
            res[freq].append(nums)


        for i in range(len(res)-1,-1,-1):
            for j in res[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        



        