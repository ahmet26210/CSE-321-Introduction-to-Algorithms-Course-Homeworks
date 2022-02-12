import math

def min_time_to_cut(N,a):
    
    global count
    if (N <= 1):
        return count
    N=N-a
    a*=2
    count+=1
    
    return min_time_to_cut(N,a)
for x in range(20):
    N=x;
    count=0
    a=1
    result= min_time_to_cut(N,a)
    print ("for",N, "rope ,neeeded cut: ",result);