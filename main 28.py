def return_index_of_min_item(arr, start_i):
  min_index = start_i
  for i in range(start_i,len(arr)):
    if arr[i] < arr[min_index]:
      min_index = i
  return min_index
  
def da_sort(nums):
  # find the elements that are already sorted example: [2,1,3,5]
  # only 1 is sorted in the above list as the 2 needs to come before 3
  
  # intialize a count to 1. if there are any items in nums,
    # at the very least the minimum element can be considered sorted.
  count = 0
  # find the index, x, of the min element in the list.
  i = return_index_of_min_item(nums, 0)
  # add the elements that come before that element to a set.
  iterated_items = set(nums[:i]) # should be noninclusive of i
  # begin loop here
  # repeat above steps except search an increasingly
  # small subarray of nums for the min_element (SEARCH: nums[i+1:])
  while i + 1 < len(nums):
    store_i = i
    i = return_index_of_min_item(nums, i+1)
    for j in range(store_i+1,i):
      iterated_items.add(nums[j])
    for n in iterated_items:
      if n < nums[i]:
        return len(nums) - 1 - count
    count+=1
  # end loop here
  return i-count

nums = [1, 3, 2, 4, 5, 6] # 4
# nums = [6,5,4,3,2,1] # 5
# nums = [1, 2, 3, 4] # 0
# nums = [5,4,3,2,1] # 4
# nums = [1, 5, 2, 4, 3, 6,7,8] # 5
print(da_sort(nums))