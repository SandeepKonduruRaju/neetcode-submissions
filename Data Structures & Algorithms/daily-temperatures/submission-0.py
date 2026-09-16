class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,num in enumerate(temperatures):
            while stack and num > stack[-1][1]:
                SI,Sdata = stack.pop()
                res[SI] = (i - SI)
                #print("i",i,"si:",SI)
            stack.append([i,num])
            #print("stack:",stack)
    
        return res