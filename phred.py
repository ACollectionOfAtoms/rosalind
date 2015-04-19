from Bio import SeqIO
import numpy as np
handle = open("this.txt", "rU")
cnt = 0
for record in SeqIO.parse(handle,"fastq"):
    if np.mean(record.letter_annotations["phred_quality"]) < 19:
        cnt += 1
    else:
        pass

print cnt
