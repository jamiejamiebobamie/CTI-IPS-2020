def server_time_check(task_config, task_times):
  task_config = task_config.split(" ")
  task_config = [int(i) for i in task_config]
  num_tasks, exec_time = task_config
  
  task_times = task_times.split(" ")
  task_times = [int(i) for i in task_times]
  index = 0

  while True:
    if exec_time - task_times[index] > 0:
      exec_time -= task_times[index]
      index+=1
    else:
      break
  return index
  
# task_config = "10 60"
# task_times = "20 7 10 8 10 27 2 3 10 5"

## Please do not change the code below this line
## These lines are how the tests interact with the code

task_config = input("Please input the number of tasks, and the maximum total execution time:")
task_times = input("Please input the execution times of each task, seperated with a space:")

print(server_time_check(task_config, task_times))
