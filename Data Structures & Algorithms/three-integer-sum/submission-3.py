class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        res = []
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                currsum = nums[i] + nums[j] + nums[k]
                #print(currsum)
                if  currsum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and  nums[j] == nums[j-1]:
                        j += 1
                    while j< k and nums[k] == nums[k+1]:
                        k -= 1
                elif currsum > 0:
                    k -= 1
                elif currsum < 0:
                    j += 1
        return res
