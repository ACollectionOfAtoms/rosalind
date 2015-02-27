def mortfib(n,m):
       life = [0]*m
       life[0] = 1
       for i in range(1,n):
           head = sum(life[1::])
           head = [head]
           tail = life[:-1]
           life = head + tail
       print sum(life) 
mortfib(81,17)
