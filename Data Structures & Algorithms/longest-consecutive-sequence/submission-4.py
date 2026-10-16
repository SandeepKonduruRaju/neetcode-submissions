class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        
        numset = set(nums)
        for num in nums:
            if (num-1) not in numset:
                counter = 1
                while num + 1 in numset:
                    num = num + 1
                    counter += 1
                    #print("num:",num,"counter:",counter)
                maxlen = max(maxlen,counter)
        return maxlen
