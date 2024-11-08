from src.aligner import globalAlignment
import argparse
from Bio import SeqIO

argParser = argparse.ArgumentParser()
argParser.add_argument("-f", "--file", dest =  "file", required=True, help = "Path to a fasta file with sequences to load" )

args = argParser.parse_args()

fasta_content = SeqIO.parse(args.file, 'fasta')

aligner = globalAlignment(seq1=next(fasta_content).seq, seq2=next(fasta_content).seq)
aligner.alignSequences()
