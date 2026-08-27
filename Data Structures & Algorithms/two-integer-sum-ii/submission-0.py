class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1

        while l < r:
            summing = numbers[l] + numbers[r]
            if summing > target:
                r-=1
            elif summing < target:
                l+=1
            else:
                return [l+1, r+1]

