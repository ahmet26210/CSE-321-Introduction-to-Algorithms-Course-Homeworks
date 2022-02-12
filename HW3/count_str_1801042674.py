def countSubstr(str, n, x, y):
    tot_count = 0
    count_x = 0

    for i in range(n):
 
        if str[i] == x:
            count_x += 1
 
        if str[i] == y:
            tot_count += count_x
    
    return tot_count
 

str = 'TXZXXJZWX'
n = len(str)
x, y = 'X', 'Z'
print('Count =', countSubstr(str, n, x, y))