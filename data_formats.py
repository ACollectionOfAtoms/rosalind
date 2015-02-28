from Bio import Entrez
from Bio import SeqIO

Entrez.email="hernandezdavid88@utexas.edu"
handle = Entrez.efetch(db="nucleotide", id=["BT149866, JX205496, NM_131329, BT149867, JQ011276, NM_001265803 ,NM_001082732 ,NM_001131214 ,NM_001003102"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format

min=100000000 
x = 0
for i in range(0,len(records)):
    if len(records[i].seq) < min:
        min = len(records[i].seq)
        x = i
print '>' + records[x].description
print records[x].seq

