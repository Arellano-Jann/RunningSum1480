def runningSum1(nums): # 7%
    final = []
    for i in range(len(nums)):
        final += [sum(nums[:i+1])]
    return final

def runningSum2(nums): # 71%
    final = [nums[0]]
    for i in range(len(nums) - 1):
        final += [final[-1] + nums[i+1]]
    return final

def runningSum(nums): # 65%
    return [sum(nums[:x+1]) for x in range(len(nums))]
        
print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))