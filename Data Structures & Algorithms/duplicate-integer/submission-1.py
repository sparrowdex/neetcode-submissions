class Solution: #Brute Force Approach
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]: #checks if both i and j are same, if same, the duplicate, making it true
                    return True
        return False
#one test case doesn't pass where the array of numbers is way too large, this has been directly added to Github as it cannot be submitted.
