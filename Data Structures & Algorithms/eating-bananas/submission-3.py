class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        r = max(piles)
        l = 1
        while l < r:
            m = (l+r)//2
            noofhours = 0
            minnoofhours = max(piles)
            for pile in piles:
                noofhours += int((pile+m-1)/m)
            if noofhours <= h:
                r = m
            else:
                l = m + 1
            
        return l
            