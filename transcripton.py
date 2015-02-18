def revc():
    dna = open('rosalind_dna.txt' , 'r')
    strand = ''
    revc = ''
    for line in dna:
        strand += line.strip()
    for item in strand:
        if item == 'A':
            revc += 'T'
        if item == 'T':
            revc += 'A'
        if item == 'C':
            revc += 'G'
        if item == 'G':
            revc += 'C'
    print revc[::-1]
revc()
