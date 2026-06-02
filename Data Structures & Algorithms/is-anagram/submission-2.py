from collections import Counter #Built in Python Tool: Counter that counts the number of characters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  #Sorting Approach
        return Counter(s) == Counter(t)
        