from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('B8DQP8')
record = SwissProt.read(handle)

print record.features
