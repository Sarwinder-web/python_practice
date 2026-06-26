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
    while index + 1 < len(nums) and nums[index]==nums[index +1]:
        index +=1
    subsets(
        nums,
        current,
        index + 1
    )
    

nums = [2,2,2,3,3]
subsets(nums,[],0)
