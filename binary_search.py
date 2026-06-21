def binary_search(lst,target,left,right):
    if left > right:
        return -1
    
    mid = ( left + right )// 2 

    if lst[mid]==target:
        return mid
    elif target > lst[mid]:
        return binary_search(lst,target,mid + 1 ,right)
    elif target < lst[mid]:
        return binary_search(lst,target,left,mid - 1)
    
print(binary_search([1,2,3,5,7,9,12,14,16,23,35],12,0,20)) 