class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for s in strs:
            encodedstr +=  str(len(s)) + "#" + s
        return encodedstr
        #print("encodedstr:",encodedstr)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenofword = int(s[i:j])
            word = s[j+1:j+1+lenofword]
            res.append(word)
            i = j + 1 + lenofword
        return res
