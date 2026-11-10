class Solution:
  def duplicateTicket(self,nums):
    l=[]
    for i in nums:
      if i in l:
        return i
      else:
        l+=[i]
        
    return -1
s=Solution()
print(s.duplicateTicket([5, 12, 1, 3, 9, 12]))
    
