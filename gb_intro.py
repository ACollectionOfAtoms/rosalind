from Bio import Entrez
Entrez.email="hernandezdavid88@utexas.edu"

handle = Entrez.esearch(db="nucleotide", term='"Rotylenchus"[Organism]', datetype = "pdat", mindate = '2001/01/10', maxdate = '2008/08/14')
record = Entrez.read(handle)
print record["Count"]
