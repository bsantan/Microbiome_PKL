#This script will convert identfied patterns from list of relationships and convert them into the specified OWL tuples with the headers "Subject", "Predicate", "Object", without brackets. 

import pandas as pd
import csv
import sys
import os
import hashlib

from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF,RDFS,OWL
from tqdm import tqdm

#from pkt_kg.utils import *

csv_filename = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OTU_Pattern_Modifications.csv"


orig_triples = pd.read_csv(csv_filename)
orig_triples = orig_triples.dropna(subset=['Pattern'])
orig_triples.fillna('N/A',inplace=True)

#Set namespace attributes
#efo = Namespace('http://www.ebi.ac.uk/efo/')
obo = Namespace('http://purl.obolibrary.org/obo/')
pkt = Namespace('http://github.com/callahantiff/PheKnowLator/pkt/')
ncbi = Namespace('http://www.ncbi.nlm.nih.gov/gene/')


pattern=[]


for idx,row in orig_triples.iterrows():
    #Always a microbe
    row['S'] =  URIRef(obo + row['S'].strip())
    row['R1'] =  URIRef(obo + row['R1'].strip())
    row['C2'] =  URIRef(obo + row['C2'].strip()) 
    row['C3'] =  URIRef(obo + row['C3'].strip()) 
    row['P'] =  URIRef(obo + row['P'].strip())
    row['E1'] =  URIRef(obo + row['E1'].strip())

    #Classes may be CHEBI or genes, which have no "_"
    row['C1'] =  URIRef(ncbi + row['C1'].strip()) if '_' not in row['C1'] and 'FAKE' not in row['C1'] else URIRef(obo + row['C1'].strip())
    if(row['Pattern'] == 2):
        pattern_string = str(row['S']) + str(row['R1']) + str(row['C2']) + str(row['R1']) + str(row['C3'])
        str_hash = URIRef(pkt + hashlib.md5(pattern_string.encode()).hexdigest())
        #Make sure all genes are integers, no decimal point
        pattern.append((str_hash,str(row['S']),str(row['C1']).replace('.0', '')))
        pattern.append((str_hash,RDFS.subClassOf,str(row['S'])))
        pattern.append((str_hash,str(row['R1']),str(row['C2'])))
        pattern.append((str_hash,str(row['R1']),str(row['C3'])))
    if(row['Pattern'] == 3):
        pattern_string1 = str(row['S']) + str(row['R1']) + str(row['C2']) + str(row['R1']) + str(row['C3'])
        pattern_string2 = str(row['P']) + str(row['E1'])
        str_hash1 = URIRef(pkt + hashlib.md5(pattern_string1.encode()).hexdigest())
        str_hash2 = URIRef(pkt + hashlib.md5(pattern_string2.encode()).hexdigest())
        pattern.append((str_hash1,str_hash2,str(row['C1'])))
        pattern.append((str_hash1,RDFS.subClassOf,str(row['S'])))
        pattern.append((str_hash1,str(row['R1']),str(row['C2'])))
        pattern.append((str_hash1,str(row['R1']),str(row['C3'])))

with open('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples.csv', 'w',newline='') as triples_file:
    writer = csv.writer(triples_file,delimiter=',')
    writer.writerow(["Subject","Predicate","Object"])
    writer.writerows(pattern)

