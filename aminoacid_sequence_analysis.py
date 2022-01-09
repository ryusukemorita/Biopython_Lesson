import os
from Bio import SeqIO
import urllib.request
import gzip
from mimetypes import guess_type
from functools import partial

urllib.request.urlretrieve("http://www.uniprot.org/uniprot/P04637.fasta", "./fasta/P04637.fasta")

fasta_file = "P04637.fasta"

with open(fasta_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)
        print(record.seq)