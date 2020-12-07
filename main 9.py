def merge_overlapping_intervals(intervals):
  change = True
  while change:
    change = False
    for i in range(len(intervals)):
      start_i, end_i = intervals[i]
      for j in range(len(intervals)):
        if j != i:
          start_j, end_j = intervals[j]
          if start_j < end_i and end_i < end_j:
            change = True
            intervals[i][1] = end_j
            intervals[j] = intervals[i]
  
  unique = set()
  for interval in intervals:
    unique.add(tuple(interval))
  answer = [list(u) for u in unique]
  answer.sort()
  return answer
    
intervals = [[1,15],[5,25],[15,40],[20,50],[55,60]]
print(merge_overlapping_intervals(intervals))