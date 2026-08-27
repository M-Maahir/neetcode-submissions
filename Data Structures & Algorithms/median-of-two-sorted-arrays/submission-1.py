class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(B) < len(A):
            A, B = B, A

        leng = len(A)+len(B)
        half = leng//2
        l = 0
        r = len(A)-1

        while True:
            m = (l + r)//2
            j = half - m - 2

            Aleft = A[m] if m >= 0 else float("-inf")
            Aright = A[m + 1] if m+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if leng%2:
                    return min(Aright, Bright)
                
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft))/2

            elif Aleft > Bright:
                r = m - 1
            else: l = m + 1

        return -1
        

