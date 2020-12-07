def merge_sorted_list(nums1, nums2):
  i = 0
  j = len(nums2) -1
  k = len(nums1) - 1
  # find the index of the first 0 in nums1
  for l in range(len(nums1)):
    if nums1[l] == 0:
      i = l - 1
      break
  while i >= 0 and j >= 0:
    if nums1[i] >= nums2[j]:
      nums1[k] = nums1[i]
      i-=1
    else:
      nums1[k] = nums2[j]
      j-=1
    k-=1
  # copy the remaining elements from one or the other arrays
  while i >= 0:
    nums1[k] = nums1[i]
    i-=1
    k-=1
  while j >= 0:
    nums1[k] = nums2[j]
    j-=1
    k-=1
  
      

 
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# print(merge_sorted_lists(nums1, nums2))
# print(nums1)