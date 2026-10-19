class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1 = defaultdict(int)

        if len(s1) > len(s2):
            return False

        for ch in s1:
            dicts1[ch] += 1


        dicts2 = defaultdict(int)
        for i in range(len(s1)):
            dicts2[s2[i]] += 1


        i = 0
        for j in range(len(s1),len(s2)):
            #print(dicts2)
            if dicts2 == dicts1:
                return True
            dicts2[s2[i]] -= 1
            if dicts2[s2[i]] == 0:
                del dicts2[s2[i]]
            i += 1
            dicts2[s2[j]] += 1
        return dicts2 == dicts1

        