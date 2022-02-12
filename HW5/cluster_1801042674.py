import math

def find_cluster(Arr,_max):
    for i,stop in enumerate(stops):
        Arr[i] = max(dictStopsVal[stop] + Arr[i-1], Arr[i])
        if Arr[i] > _max:
            _max = Arr[i]
    return _max

stops = ["A","B","C","D","E","F","G"]
dictStopsVal = {"A":3, "B":-5, "C":2, "D":11, "E":-8, "F":9, "G":-5}
Arr = [0,0,0,0,0,0,0,0]
_max = -math.inf
print(find_cluster(Arr,_max))
