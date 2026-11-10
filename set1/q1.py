class Solution():
  def giftcard(self,total,nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
          return i , j
s=Solution()
print(s.giftcard(6,[120, 45, 80, 200, 35, 150],235))
    
