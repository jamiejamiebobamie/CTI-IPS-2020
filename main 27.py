
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem
def color_sort(nums):
  i = 0
  j = 0
  k = len(nums)-1
  while j < k:
    if nums[j]<1:
      nums[i], nums[j] = nums[j], nums[i]
      i+=1
      j+=1
    elif nums[j]>1:
      nums[j], nums[k] = nums[k], nums[j]
      k-=1
    else:
      j+=1
  return nums

nums = [0,1,0,1,2,1]
print(color_sort(nums))
