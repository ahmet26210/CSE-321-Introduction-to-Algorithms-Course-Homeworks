import sys
 
def findWorstAndBest(nums, left, right, min=sys.maxsize, max=-sys.maxsize):

 
    if left == right:              
 
        if min > nums[right]:        
            min = nums[right]
 
        if max < nums[left]:           
            max = nums[left]
 
        return min, max
 

    if right - left == 1:          
 
        if nums[left] < nums[right]:     
            if min > nums[left]:       
                min = nums[left]
 
            if max < nums[right]:      
                max = nums[right]
 
        else:
            if min > nums[right]:     
                min = nums[right]
 
            if max < nums[left]:     
                max = nums[left]
 
        return min, max
 
  
    mid = (left + right) // 2
 
 
    min, max = findWorstAndBest(nums, left, mid, min, max)
 

    min, max = findWorstAndBest(nums, mid + 1, right, min, max)
 
    return min, max
 
 
if __name__ == '__main__':
 
    nums = [7, 2, 9, 3, 1, 6, 7, 8, 4]
 
    (worst, best) = findWorstAndBest(nums, 0, len(nums) - 1)
 
    print("The worst element in the list is", worst)
    print("The best element in the list is", best)