from __future__ import division
def gccontent():
    f0 = open('rosalind_gc.txt' , 'r').read()
    f = f0.replace("\n", "")
    d = {}
    d2 = {}
    each0 = f.split('>')
    each = each0[1:]
    for item in each:
        d[item[:13]] = item[13:]
    for k , v in d.items():
        total = len(v)
        GC = 0
        for nuc in v:
            if nuc == 'C' or nuc == 'G':
                GC += 1
            else:
                pass
        d2[k] = round((GC/total)*100, 7)
    print d2
gccontent()
