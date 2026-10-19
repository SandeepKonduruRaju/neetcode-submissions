class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            print(l,r,mid)
            if l == r == mid:
                return nums[mid]
            elif nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
