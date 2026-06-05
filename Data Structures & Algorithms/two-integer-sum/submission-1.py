class Solution: #Optimized Approach : HashMaps
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={} #Stores value: index

        #enumerate gives us both index (i) and the actual number (num)
        for i, num in enumerate (nums):
            complement = target - num

            #if the matching partner is already in our map , we will find the pair
            if complement in seen:
                return [seen[complement], i]
            # otherwise, save the current number and its index into the map
            seen[num]=i