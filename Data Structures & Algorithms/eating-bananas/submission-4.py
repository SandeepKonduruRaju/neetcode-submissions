class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = max(piles)
        mink = float('inf')
        while l <= r:
            mid = (l+r)//2
            currsum = 0
            for i in range(len(piles)):
                currsum += (piles[i]+mid-1)//mid
            print("currsum",currsum,"mid:",mid)
            if currsum <= h:
                mink = min(mink,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return mink