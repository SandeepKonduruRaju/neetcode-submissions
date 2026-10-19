class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'{':'}','[':']','(':')'}
        for ch in s:
            if ch in dict:
                stack.append(ch)
                print(stack)
            else:
                if stack:
                    print("ele block")
                    poppedele = stack.pop()
                    popkeyele = dict[poppedele]
                    print(poppedele,popkeyele)
                    if ch != popkeyele:
                        return False
                else:
                    return False
        return len(stack) == 0