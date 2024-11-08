from src.aligner import globalAlignment
import argparse
from Bio import SeqIO

argParser = argparse.ArgumentParser()
argParser.add_argument("-f", "--file", dest =  "file", required=True, help = "Path to a fasta file with sequences to load" )
argParser.add_argument("-m", "--match", dest =  "match", required=False, default=1, help = "set match score", type=int )
argParser.add_argument("-s", "--mismatch", dest =  "mismatch", required=False, default=-1, help = "set mismatch score", type=int )
argParser.add_argument("-g", "--gap", dest =  "gap", required=False, default=-2, help = "set gap penalty", type=int )

args = argParser.parse_args()

fasta_content = SeqIO.parse(args.file, 'fasta')

aligner = globalAlignment(seq1=next(fasta_content).seq, seq2=next(fasta_content).seq, matchScore=args.match, mismatchScore=args.mismatch, gapPenaltyScore=args.gap)
aligner.alignSequences()
