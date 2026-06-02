class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  #Sorting Approach
        if len(s)!=len(t):  #if length doesn't match, no way can they be an anagram
            return False
        return sorted(s) == sorted(t)
        