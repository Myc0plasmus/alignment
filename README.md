# Python script for aligning two sequences

## Description

This script performs global alignment of two sequences based using needleman-wunsch algorithm. 

## Prerequisites 

Script uses biopython to load fasta files, therefore biopython needs to be installed:

```pip3 install biopython```

## Usage

The program should be run via command:

python main.py -f <path to file>

* script should be executed from project root directory
* file should be in fasta format and contain exactly two sequences to be aligned

## Output

The program will output the alignemt along with its score

This is output from example test.fasta
A T G _
| . |  
A C G T
alignment score: -1

The two sequences are aligned, "_" in the sequence signifies a gap, between two sequences there is an additional line, empty space in it signifies a gap, a dot "." signifies a mismatch and "|" signifies a match
