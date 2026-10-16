class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedword = tuple(sorted(word))
            if sortedword not in dict:
                dict[sortedword] = []
            dict[sortedword].append(word)
        return list(dict.values())
            