class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        h = len(height)
        #go to current height, find biggest to left and right of it,
        #then subtract current height from whats the smaller left and right max
        for i in range(h):
            lMax = rMax = height[i]
            for j in range(i):
                #print("hj", height[j])
                #print("lmax", lMax)
                lMax = max(lMax, height[j])
                #max of lMax and current height
            for k in range(i + 1, h):
                #print("hk", height[k])
                #print("rmax", rMax)
                rMax = max(rMax, height[k])
                #iterate through heights to find rMax
            result += min(lMax, rMax) - height[i]
            #result adds all the shit
        return result