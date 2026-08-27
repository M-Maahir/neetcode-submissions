class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        size = 0
        end = 0
        hsmp = {}
        res = []

        for i, v in enumerate(s):
            hsmp[v] = i
        
        for i, v in enumerate(s):
            size += 1

            end = max(end, hsmp[v])

            if i == end:
                res.append(size)
                size = 0

        return res   


        