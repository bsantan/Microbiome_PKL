#This script will convert the triples generated by Convert_Patterns of Subject/Predicate/Object headers to contain brackets.

import pandas as pd
import csv

#input_file = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/OWLNETS_Triples.csv'
#input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_OWLNETS_Triples.csv'
#input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples.csv'
#input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples_Updated.csv'
#input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/microbes_Triples.csv'
#input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutmgene_microbes_Triples.csv'
input_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples.csv'


orig_file = pd.read_csv(input_file)

orig_file["Subject"] = '<'+orig_file["Subject"]+'>'
orig_file["Predicate"] = '<'+orig_file["Predicate"]+'>'
orig_file["Object"] = '<'+orig_file["Object"]+'>'

#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/OWLNETS_Triples_Brackets.txt',sep='\t',index=False)
#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_OWLNETS_Triples_Brackets.txt',sep='\t',index=False)
#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples_Brackets.txt',sep='\t',index=False)
#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples_Updated_Brackets.txt',sep='\t',index=False)
#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/microbes_Triples_Brackets.txt',sep='\t',index=False)
#orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutmgene_microbes_Triples_Brackets.txt',sep='\t',index=False)
orig_file.to_csv('/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples_Brackets.txt',sep='\t',index=False)

