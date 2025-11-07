import numpy as np
arr=[-2, -1, -3, -4, -1, -2, -1, -5, -4]


subs=[]
try:
    for i in range(len(arr)):
        cs=0
        for j in range(i,len(arr)):
            #print(f'{cs}+{arr[j]}')
            cs+=arr[j]
            subs.append(cs)

        #print(cs)

    res=np.array(subs).max()
    if res<0:
        print(0)
    else:
        print(res)
except:
    print(0)
