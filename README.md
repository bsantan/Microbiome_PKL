# Microbiome_PKL
Incorporating GutMGene into PheKnowLator

#To add only gutMgene in PKL

#Functions in gutMGene_PKLAddition_NoRotation.ipynb

#Get_gutMgene_microbes to generate gutMgene_microbes_updated.csv, metab_microbes_updated.csv, and gene_microbes_updated.csv for each of the KGs you want to integrate (i.e. both metabs and genes or only one or the other)- updated all names of microbes to align with original or new name, as there were inconsistencies among the files themselves

#Create_URI_Label_Map_GutMGene to create gutMGene_URI_LABEL_MAP.csv

#Generate_patterns_GutMgene_only - new to create gutMGene_OTU_Pattern_Modifications.csv

#Create_microbe_relationships_gutMGene to create gutmgene_microbes_Triples.csv

python GutMGene_Convert_Patterns.py (/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene)
- updated to input gutMGene_OTU_Pattern_Modifications.csv and output gutMGene_OWLNETS_Triples.csv

python Add_Brackets.py (~/Documents/Rotation2/TiffanyFiles/Node2Vec/)
#This is only necessary if new microbe/metab or other interactions were added
- updated to take in gutMGene_OWLNETS_Triples.csv and output gutMGene_OWLNETS_Triples_Brackets.txt
- updated to take in gutmgene_microbes_Triples.csv and output gutmgene_microbes_Triples_Brackets.txt

python concat_files.py
- updated to take in gutMGene_OWLNETS_Triples_Brackets.txt and gutmgene_microbes_Triples_Brackets.txt and output gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt 
- updated to take in PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt and gutMGene_and_microbes_OWLNETS_Triples_Brackets.txt and output PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withGutMGene_withMicrobes.txt


python Nodes2Integers.py 
Update to take in PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withGutMGene_withMicrobes.txt
 And output 
	⁃	- PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withGutMGene_withMicrobes.txt
	⁃	- PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withGutMGene_withMicrobes.json
	⁃	- PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_withGutMGene_withMicrobes.txt
