class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        st = set()
        l = 0

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1

            w = (r - l) + 1
            length = max(w, length)
            st.add(s[r])
        
        return length

