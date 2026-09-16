class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'}':'{',']':'[',')':'('}
        stack = []
        for ch in s:
            if ch  in dict.values():
                stack.append(ch)
                #print("stack:",stack)
            else:
                if stack:
                    popedele = stack.pop()
                    pairingele = dict[ch]
                    print("popedele:",popedele,"pairingele:",pairingele)
                    if popedele != pairingele:
                        return False
                else:
                    return False
        return len(stack) == 0
        