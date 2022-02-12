def candy(arr, n,Arr1):

    for i in range(1, n+1):
        max_val = -1
        for j in range(i):
             max_val = max(max_val, arr[j] + Arr1[i-j-1])
        Arr1[i] = max_val

    return Arr1[n]

Arr1 = [0,0,0,0,0,0,0,0,0]
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(candy(arr, size,Arr1)))
