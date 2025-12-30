
def qurp(nums,target):
    #nums = input('Please enter and array of enterger')
    Fnums =[]
    #target = input('PLease enter the target')
    n = len(nums)

    for a in range(n-3):
        for b in range(a+1, n-2):
            for c in range(b+1, n-1):
                for d in range(c+1,n):
                    if nums[a]+nums[b]+nums[c]+nums[d]== target:
                        Fnums.append([nums[a], nums[b], nums[c], nums[d]])
    return Fnums

qurp([1,2,3,4,5,4,6,3,7,2,6,1,3,2,4,5,6,7,2,1,3,4,3,7],10)
    



