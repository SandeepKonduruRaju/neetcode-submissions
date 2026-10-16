class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        output= len(nums) * [1]
        
        for i in range(len(nums)):
            output[i] = prefix * output[i]
            prefix = nums[i] * prefix
        #print(output)
        suffix = 1
        for j in range(len(nums)-1,-1,-1):
            output[j] = output[j] * suffix
            suffix = suffix * nums[j]
            

        return output