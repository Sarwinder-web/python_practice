def subsets(nums,current,index):
    if index==len(nums):
        print(current)
        return 
    
    current.append(nums[index])
    subsets(
        nums,
        current,
        index + 1
    )
    current.pop()
    subsets(
        nums,
        current,
        index + 1
    )
nums = [1,2,3]
subsets(nums,[],0)