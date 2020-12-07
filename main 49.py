# O(n) space
# O(n) time
def single_number(nums):
  unique = {}
  for num in nums:
    if num not in unique:
      unique[num] = 1
    else:
      unique[num] += 1
  for key,val in unique.items():
    if val != 3:
      return key

# O(1) space
# O(nlogn) time
"""
def single_number(nums):
  nums.sort()
  count = 0
  for i in range(len(nums)-1):
    # keep count if items are the same
    if nums[i] == nums[i+1]:
      count+=1
    else:
      # if items are not the same and the count equals 0
        # the first item of nums is unique
      if count == 0:
        return nums[i]
      # if items are not the same and the count equals 1
        # the last item iterated over is unique  
      elif count == 1:
        return nums[i-1]
  # check the last element of the array as the above for-loop doesn't iterate over it.
  if nums[len(nums)-1] != nums[len(nums)-2]:
    return nums[len(nums)-1]
"""