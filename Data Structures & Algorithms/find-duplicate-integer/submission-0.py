class Solution:
    def findDuplicate(self, nums: List[int]) -> int:


        slow = nums[0]
        fast = nums[0]
        # Phase 1: Find meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Phase 2: Find cycle entrance (duplicate)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        
        return slow