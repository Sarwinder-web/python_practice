def permutations(nums, current, used):
    if len(current)==len(nums):
        print(current)
        return 
    
    for i in range(len(nums)):
        if not used[i]:
            current.append(nums[i])
            used[i] = True
            permutations(nums,current,used)
            current.pop()
            used[i] = False

nums = [1,2,3]

used = [False]*len(nums)

permutations(nums,[],used)
    

