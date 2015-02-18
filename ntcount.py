def transcription():
    dna = open('rosalind_rna.txt' , 'r')
    strand = ''
    count = {}
    for line in dna:
        strand += line.strip()
    for itme in strand:
        print itme
ntcount()
