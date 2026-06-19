def subsets(nums,index,current):
    if index==len(nums):
        print(current)
        return 
    
    current.append(nums[index])
    subsets(
        nums,
        index +1,
        current
    )

    current.pop()

    subsets(
        nums,
        index +1,
        current
    )
nums = [1,2,3]
subsets(nums,0,[])
