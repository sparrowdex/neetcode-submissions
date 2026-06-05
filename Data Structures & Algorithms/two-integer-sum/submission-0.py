class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Loop through every index in the array:
        for i in range(len(nums)):
            #Loop through every index after i (this automatically checks in i==j)
            for j in range (i+1, len(nums)):
                #Check if the values at these indices equal the target
                if nums[i] + nums[j] == target:
                    return [i,j]
        #this is O(n^2) because it will get real slow if a massive array is given as input