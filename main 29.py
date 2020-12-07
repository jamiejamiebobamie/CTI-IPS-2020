def merge(arr1,arr2,arr):
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      arr[i+j] = arr1[i]
      i+=1
    elif arr1[i] > arr2[j]:
      arr[i+j] = arr2[j]
      j+=1
    else:
      arr[i+j] = arr1[i]
      i+=1
      arr[i+j] = arr2[j]
      j+=1
  # add the remaining elements from either arr1 or arr2
  while i < len(arr1):
      arr[i+j] = arr1[i]
      i+=1
  while j < len(arr2):
      arr[i+j] = arr2[j]
      j+=1
  return arr
  
def merge_sort(arr):
  if len(arr) == 1:
    return
  mid = len(arr)//2
  arr1 = arr[0:mid]
  arr2 = arr[mid:]
  merge_sort(arr1)
  merge_sort(arr2)
  merge(arr1,arr2,arr)
  return arr
# nums = [1,4,5,2,7,8,3]
# print(merge_sort(nums))