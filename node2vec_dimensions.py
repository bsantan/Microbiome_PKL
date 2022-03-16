

import node2vec
import os

os.chdir('/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec')

edgelist = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/Node2Vec_DimensionCheck/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_withGutMGene_withMicrobes.txt'
#edgelist = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/Node2Vec_DimensionCheck/test_edgelist.txt'

for j in range(0,1):
    #for i in range(2,128,4):
    for i in [42]:
        command =  "python sparse_node2vec_wrapper_dimOutput.py --edgelist {} --dim {} --walklen 10 --walknum 20 --window 10 --iteration {}"  #
        os.system(command.format(edgelist,i,j))  