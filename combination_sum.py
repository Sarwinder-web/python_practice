def combination_sum(nums,target,index,current):

    if sum(current)==target:
        print(current)
        return 
    
    if sum(current)>target:
        return
    
    if index==len(nums):
        return
    
    current.append(nums[index])

    combination_sum(nums,target,index,current)

    current.pop()

    combination_sum(nums,target,index+1,current)

nums = [5,6,9]
target = 56

combination_sum(nums,target,0,[])

