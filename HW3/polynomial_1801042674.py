def BruteForceAlgorithm(arr, n, x):
    a = 0
    i=n
    j = 1
    k=0
    
    while i > 0:
        
        power=1
        j=1
        while j < i:
            power=power*x
            j+=1
            
        a=a+arr[k]*power
        
        k+=1
        i-=1
    return a
 

b = [2, 2, 5] # -> 2x^2+2x+5      #2x^2+5 -> b =[2,0,5]
y=len(b)
print('Count =', BruteForceAlgorithm(b, y, 3))