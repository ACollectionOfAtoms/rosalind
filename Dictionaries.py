def main():
    s = open('rosalind_ini6.txt', 'r')
    t = ''
    for line in s:
        line.strip()
        t += line
    l = t.split()
    z = {}
    for item in l:
        if item in z:
            z[item] += 1
        else:
            z[item] = 1

    s.close()

    o = open('output.txt' , 'w')
    for item in z:
        this = item + ' ' +  str(z[item]) + '\n'
        o.write(this)
    o.close()




main()
