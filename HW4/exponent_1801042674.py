def power(x,y):
     temp=0
     
     if( y ==1):
        return x
     if( y ==0):
        return 1
     if (y%2 == 0):
      temp = power(x, y/2)
      return temp*temp
     
     else:
       temp = power(x, (y-1)/2)
       return x*temp*temp
     
a=2
b=3
result= power(a,b)
print(result)