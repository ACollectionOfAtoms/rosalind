import collections
def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        tmp1 = 1
        tmp2 = 1
        z = 0
        for i in range(1,x-1):
            z = tmp1 + tmp2
            tmp1 = tmp2
            tmp2 = z
    return z
def ghostdeath(n,m,k,j):
    #Modify this to omit values greater than n!
    #This has been completed with the j variable.
    maxi = j
    deaths = {}
    ghostdeath = {}
    for i in range(1,n-m):
        deaths[m+k+i] = -fib(i)
    for z in deaths:
        if z <= j:
            ghostdeath[z] = deaths[z]
        else:
            pass
    #return deaths
    return ghostdeath
def mortfib(n,m):
    alive = fib(n)
    deaths = {m:1, m+1:0}
    deathbook = []
    print alive , 'Alive, un-modified'
    print deaths , 'Initial deaths'
    print deathbook , 'Initial deathbook'
    #position of first birth starts at n = 3.
    #e.g fib(3) = 2, 1 of which is a birth.
    if n <= m:
        return fib(n)
    else:
        for i in range(1,n-m):
            deaths[m+i+1] = fib(i)
        print deaths , 'Deaths position, and number of deaths added including ghost\n'
        # modify death dictionary, removing
        # ghost deaths.
        # first, account for ghost deaths!
        # ********** There's something wrong with the length of the dicts, or list of dicts******
        for k in deaths:
            if k != m + 1:
                #print n-k+1 , m , k , n
                deathbook.append(ghostdeath(n-k,m,k,n))
        print deathbook , 'Deathbook with no modification\n'
        deathbook = filter(None,deathbook)
        print deathbook , 'Deathbook, cleared of empty dictionaries\n'
        sumofghost = collections.Counter()
        for d in deathbook:
            sumofghost.update(d)
        print sumofghost , 'Sum of all ghost deaths\n'
        print deaths , 'Original deaths\n'
        sumofghost.update(deaths)
        deaths = sumofghost
        deaths.pop(n,None)
        print deaths , 'Updated deaths\n'

        for k in deaths:
            if k != m + 1:
                alive -= fib(n-k+1)*deaths[k]
        # something happens with large numbers
        # subtraction is incorrect, the larger
        # n is! n = 13, m = 3
        return alive
print mortfib(13,3)
