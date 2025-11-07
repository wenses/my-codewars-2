def maxsubsum(arr):
    me=arr[0]
    res=arr[0]

    if len(arr)==0:
        res=0
    else:
        for i in range(1,len(arr)):

            me=max(me+arr[i],arr[i])

            res=max(res,me)
        if res<0:
            res=0

    return res


print(maxsubsum([0]))
