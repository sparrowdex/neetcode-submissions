class Solution:
    def hasDuplicate(self, nums):
        seen=set() #this solution makes use of a set, as set can only contain unique values
        for value in nums:
            if value in seen:
                return True
            seen.add(value)
        return False