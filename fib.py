def fib(n, k):
  if n == 0:
      return 0
  if n==1:
    return 1
  else:
    return k*fib(n-2, k) + fib(n-1, k)

print fib(22,1)
