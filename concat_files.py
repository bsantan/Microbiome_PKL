#This script will take bracketed tuples as inputs and concatenate them into a new list of tuples. Headers must be "Subjet", "Predicate", "Object"

import pandas as pd
import csv
import sys
import os

#filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt', '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/OTUs_Tuples.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt', '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/OWLNETS_Triples_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_OWLNETS_Triples_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_OWLNETS_Triples_Brackets.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_OWLNETS_Triples_Brackets.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/microbes_Triples_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/OWLNETS_Triples_updated_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/Rotation_and_GutMGene_and_microbes_OWLNETS_Triples_Brackets.txt']
#filenames = ['/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples_Brackets.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutmgene_microbes_Triples_Brackets.txt']
filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt']



#filenames = ['/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt','/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/Rotation_and_GutMGene_and_microbes_OWLNETS_Triples_Brackets.txt']

#with open("/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs_withGutMGene.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/Rotation_and_GutMGene_OWLNETS_Triples_Brackets.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/Rotation_and_GutMGene_and_microbes_OWLNETS_Triples_Brackets.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs_withGutMGene_withMicrobes.txt","w") as outfile:
#with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt","w") as outfile:
with open("/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withGutMGene_withMicrobes.txt","w") as outfile:
    with open(filenames[0]) as f1:
        for line in f1:        #keep the header from file1
            outfile.write(line)

    for x in filenames[1:]:
        with open(x) as f1:
            for line in f1:
                if not line.startswith("Subject"):
                    outfile.write(line)

