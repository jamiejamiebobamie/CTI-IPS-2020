# Although you cannot see it, imagine there is a function called isBadVersion already defined.
# the automatic tests will account for it
# here is an example implementation, although the tests will have a different actual value
# the first bad version won't always be 7, but the other function will behave similarly

# def isBadVersion(version):
#   return version > 7
# when you run your tests, comment this function out.

def firstBadVersion(last_version, isBadVersion):
  for n in range(last_version):
    if isBadVersion (n):
      return n