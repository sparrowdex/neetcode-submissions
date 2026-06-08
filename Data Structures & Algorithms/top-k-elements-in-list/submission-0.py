class Solution: #O(n) optimal solution without external library exports
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count character frequencies
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # Step 2: Create buckets array where index = frequency
        # We need len(nums) + 1 slots to handle index up to len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in count_map.items():
            buckets[count].append(num)

        # Step 3: Iterate backwards from the highest frequency bucket
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                # Once we have grabbed k elements, return the list immediately
                if len(res) == k:
                    return res