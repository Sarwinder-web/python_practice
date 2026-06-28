def combination_sum(nums,current,index,target):
    if target==0:
        print(current)
        return
    
    if  target < 0:
        return
    
    if index == len(nums):
        return
    
    current.append(nums[index])

    combination_sum(nums,current,index,target - nums[index])

    current.pop()

    combination_sum(nums,current,index + 1, target)

nums = [1,2,3,4]
combination_sum(nums,[],0,7)

