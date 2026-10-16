class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dictfreq = defaultdict()
        for num in nums:
            dictfreq[num] = dictfreq.get(num,0) + 1
        sorteddict = sorted(dictfreq.items(),key = lambda x :x [1],reverse = True)
        #print(dictfreq)
        #print(sorteddict)
        for i in range(k):
            res.append(sorteddict[i][0])
        return res
        