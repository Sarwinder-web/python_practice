def permutation(nums,current,visited):
    if len(current)==len(nums):
        print(current)
        return
    for i in range(len(nums)):
        if not visited[i]:
            current.append(nums[i])
            visited[i] = True
            permutation(nums,current,visited)
            current.pop()
            visited[i] = False
    return True 
nums = [1,2,3]
visited = [False]*len(nums)
# count permutation 
def count_permutation(nums,current,visited):
    if len(current)==len(nums):
        return 1

    count = 0
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i]= True 
            current.append(nums[i])
            count +=count_permutation(nums,current,visited)
            current.pop()
            visited[i]= False
        
    return count 

nums = [1,2,3]

visited = [False] * len(nums)

print(count_permutation(nums, [], visited))

def result_permutation(nums,current,visited):
    if len(current)==len(nums):
        return [current.copy()]
    result = []

    for i in range(len(nums)):
        if not visited[i]:
            visited[i]=True
            current.append(nums[i])
            result +=result_permutation(nums,current,visited)
            current.pop()
            visited[i]=False

    return result 
nums = [1,2,3]

visited = [False]*len(nums)

print(result_permutation(nums,[],visited))
