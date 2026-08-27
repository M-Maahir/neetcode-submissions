class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        ls1 = [0]*26

        for i in range(len(s)):
            ls1[ord("a") - ord(s[i])] += 1
            
            ls1[ord("a") - ord(t[i])] -= 1

            print(ls1[ord(s[i]) - ord("a")])
        

        for i in range(len(ls1)):
            if ls1[i] != 0:
                return False
        
        return True
        