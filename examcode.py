#In order to run this blast program, you need to type the code below into the terminal
#./examcode.py -q queryfile.fasta -r referencefile.fasta
#queryfile.fasta stands for your query sequences file
#referencefile.fasta stand for your reference sequences file
#===================================================== BLAST PROGRAM =========================================================
#!/usr/bin/python3
#Import modules that will be used
import sys 
import os 
import argparse  
#Function that let users input the type of query sequence and reference sequence for blast mode determination
def info():
    global query,reference
    query = input("Please input the type of query sequence (prot/nucl):")
    reference = input("Please input the type of reference sequence (prot/nucl):")
#Function that uses input parameters
def _argparse():
    parser = argparse.ArgumentParser(description="A local BLAST wrapper")
    parser.add_argument('-q', '--query', action='store', dest='query', required=True, help='query file should be fasta format')
    parser.add_argument('-r', '--reference', action='store', dest='reference', required=True, help='reference file should be fasta format')
    return parser.parse_args() 
#Function that runs blastn
def blastn():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    #First step: make BLAST database.
    os.system("makeblastdb -parse_seqids -dbtype nucl -in {} -out ./Plasmodium_db".format(reference))
    #Second step: Run BLAST and save the reult in file blastn.out.
    os.system("blastn -db ./Plasmodium_db -query {} -out blastn.out -outfmt 7 -num_threads 20".format(query))
    print("all done!") 
#Function that runs blastx
def blastx():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype prot -in {} -out ./Plasmodium_db".format(reference))
    os.system("blastx -db ./Plasmodium_db -query {} -out blastx.out -outfmt 7 -num_threads 20".format(query))
    print("all done!")
#function that runs tblastn
def tblastn():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype nucl -in {} -out ./Plasmodium_db".format(reference))
    os.system("tblastn -db ./Plasmodium_db -query {} -out tblastn.out -outfmt 7 -num_threads 20".format(query))
#Function that runs blastp()
def blastp():
    parser = _argparse()
    query = parser.query
    reference = parser.reference
    os.system("makeblastdb -parse_seqids -dbtype prot -in {} -out ./Plasmodium_db".format(reference))
    os.system("blastp -db ./Plasmodium_db -query {} -out blastp.out -outfmt 7 -num_threads 20".format(query))
#Run the function info() for querying infomation
info()
#According to different query and reference type, run different blast functions
if query == 'nucl' and reference == 'nucl': 
    blastn()
if query == 'nucl' and reference == 'prot':
    blastx()
if query == 'prot' and reference == 'nucl':
    tblastn()
if query == 'prot' and reference == 'prot':
    blastp()
#========================================================= END ==============================================================
