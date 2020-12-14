#!/usr/bin/python3
import sys 
import os 
import argparse 
#def usage(): 
 #   python local.blast.py -h
  #  example:
   #     pythonlocal.blast.py -q your.query.fa -r reference.fa
   # pass 
def info():
    global query,reference
    query = input("Please input the type of query sequence (prot/nucl):")
    reference = input("Please input the type of reference sequence (prot/nucl):")

def _argparse():
    parser = argparse.ArgumentParser(description="A local BLAST wrapper")
    parser.add_argument('-q', '--query', action='store', dest='query', required=True, help='query file should be fasta format')
    parser.add_argument('-r', '--reference', action='store', dest='reference', required=True, help='reference file should be fasta format')
    return parser.parse_args() 

def blastn():
  #Download Plasmodium simium reference from NCBI. reference should be fasta format."""
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    # first step: make BLAST database.
    os.system("makeblastdb -parse_seqids -dbtype nucl -in {} -out ./Plasmodium_db".format(reference))
    # second step: Run BLAST.
    os.system("blastn -db ./Plasmodium_db -query {} -out blastn.out -outfmt 7 -num_threads 20".format(query))
    print("all done!") 

def blastx():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype prot -in {} -out ./Plasmodium_db".format(reference))
    os.system("blastx -db ./Plasmodium_db -query {} -out blastx.out -outfmt 7 -num_threads 20".format(query))
    print("all done!")

def tblastn():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype nucl -in {} -out ./Plasmodium_db".format(reference))
    os.system("tblastn -db ./Plasmodium_db -query {} -out tblastn.out -outfmt 7 -num_threads 20".format(query))

def blastp():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype prot -in {} -out ./Plasmodium_db".format(reference))
    os.system("blastp -db ./Plasmodium_db -query {} -out blastp.out -outfmt 7 -num_threads 20".format(query))

info()
if query == 'nucl' and reference == 'nucl': 
    blastn()
if query == 'nucl' and reference == 'prot':
    blastx()
if query == 'prot' and reference == 'nucl':
    tblastn()
if query == 'prot' and reference == 'prot':
    blastp()

