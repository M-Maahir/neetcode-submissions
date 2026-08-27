class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dics = {}

        count = [[] for i in range(len(nums)+1)]

        res = []

        for i in nums:
            dics[i] = dics.get(i,0) + 1

        for num, freq in dics.items():
            count[freq].append(num)


        for i in range(len(count)-1,-1,-1):
            for j in count[i]:
                res.append(j)
                if k == len(res):
                    return res





        