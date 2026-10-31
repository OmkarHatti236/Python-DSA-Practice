def trapped(heigth):
    #left max values
    n=len(heigth)
    leftMax=[0]*n
    
    leftMax[0]=heigth[0]
    for i in range(1,n):
        maxvalue=max(leftMax[i-1],heigth[i])
        leftMax[i]=maxvalue
    print("leftmaxes:",leftMax)
    #rightmax value
    rightmax=[0]*n
    rightmax[n-1]=heigth[n-1]
    for i in range(n-2,-1,-1):
        maxvalue=max(rightmax[i+1],heigth[i])
        rightmax[i]=maxvalue
    print("heights:",heigth)
    print("rightmaxes:",rightmax)
    trappedWater=0
    for i in range(n):
        level=min(leftMax[i],rightmax[i])-heigth[i]
        trappedWater+=level
    
    print("Total trapped water:",trappedWater)



heigth=[4,2,0,6,3,2,5]
trapped(heigth)