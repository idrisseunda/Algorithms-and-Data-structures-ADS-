def color(nums):
   subRed = []
   subWhite = []
   subblue = []
   fnums = []

   n = len(nums)
   
   for i in range(n):
            if nums[i] == "red":
                subRed.append(nums[i]) 
            elif nums[i] == "white":
                subWhite.append(nums[i])
            else :
                subblue.append(nums[i])
   fnums.append(subRed)
   fnums.append(subWhite)
   fnums.append(subblue )
   return fnums

print(color(["white","red","blue","blue","red","blue","white","red","red","white","blue","red"]))