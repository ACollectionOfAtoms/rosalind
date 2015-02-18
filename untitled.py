def fib(n,k):
    a = n
    b = k
for i in range(b*(a- 1)):
    a,b = b,a+b
  return a

print fib(5,3)
