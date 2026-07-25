class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longeststreak = 0
        for num in numsets:
            streak = 0
            #to find begn ele
            if num - 1 not in numsets:
                curr_num = num
                streak += 1

                #to find streak of consecutive ele
                while curr_num + 1 in numsets:
                    curr_num +=  1
                    streak += 1
                    print(curr_num,streak)
                    
                print("longeststreak:",longeststreak,"streak:",streak)
                longeststreak = max(longeststreak,streak)
        return longeststreak
