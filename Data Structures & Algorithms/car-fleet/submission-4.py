class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timezip = list(zip(position,speed))
        sortedtimezip = sorted(timezip,reverse= True)
        stack = []
        timetaken = 0
        #print(sortedtimezip)
        for num in sortedtimezip:
            timetaken = (target - num[0])/num[1]
            #print("timetaken:",timetaken)
            if not stack:
                stack.append(timetaken)
                #print("stack:",stack)
            
            elif timetaken > stack[-1]:
                #print(timetaken,stack[-1])
                stack.append(timetaken)
                #print("stack val",stack)
        return len(stack)
        