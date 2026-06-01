class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick exit: Different lengths mean they can't be anagrams
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # Build the frequency dictionaries
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        # Compare the two dictionaries
        return countS == countT