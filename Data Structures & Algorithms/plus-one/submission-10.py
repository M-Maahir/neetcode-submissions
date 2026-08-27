class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        s = ""    
        for i in digits:
            s += (str(i))
        
        res = int(s) + 1

        ls = []
        
        for i in str(res):
            ls.append(int(i))
        
        return ls

        