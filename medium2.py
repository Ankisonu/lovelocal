def all_Element(nums):
    count1, count2 = 0, 0
    element1, element2 = None, None
    
    for num in nums:
        if num == element1:
            count1 += 1
        elif num == element2:
            count2 += 1
        elif count1 == 0:
            element1 = num
            count1 = 1
        elif count2 == 0:
            element2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
            
    count1, count2 = 0, 0
    for num in nums:
        if num == element1:
            count1 += 1
        elif num == element2:
            count2 += 1
            
    result = []
    if count1 > len(nums) // 3:
        result.append(element1)
    if count2 > len(nums) // 3:
        result.append(element2)
        
    return result

nums = [3,2,3]
print(all_Element(nums))
