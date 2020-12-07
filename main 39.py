test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  log = {}
  for entry in logs:
    words = entry.split(' ')
    error_category = words[0][1:-1]
    error_code = words[1]
    for i in range(len(words)):
      if words[i][-1] == ":":
        break
    error_title = " ".join(words[2:i+1])[:-1]
    error_message = " ".join(words[i+1:])
    if error_category not in log:
      log[error_category] = {error_code:{error_title:{error_message:1}}}
    else:
      if error_code not in log[error_category]:
        log[error_category][error_code] = {error_title:{error_message:1}}
      else:
        if error_title not in log[error_category][error_code]:
          log[error_category][error_code][error_title] = {error_message:1}
        else:
          if error_message not in log[error_category][error_code][error_title]:
            log[error_category][error_code][error_title][error_message] = 1
          else:
            log[error_category][error_code][error_title][error_message] += 1
  return log

print(log_stats(test_data))