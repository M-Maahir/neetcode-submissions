class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        ln = len(A)+len(B)

        mid = ln // 2

        if len(B) < len(A):
            A, B = B, A

        r = len(A)-1
        l = 0

        while True:

            i = (r+l)//2
            j = mid - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Anext = A[i+1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bnext = B[j+1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bnext and Bleft <= Anext:
                if ln % 2:
                    return min(Anext, Bnext)
                x = (max(Aleft, Bleft) + min(Anext, Bnext))/2
                return x
            elif Aleft > Bnext:
                r = i - 1
            else:
                l = i + 1



        