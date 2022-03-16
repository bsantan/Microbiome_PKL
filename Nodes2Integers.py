import json
from tqdm import tqdm

# read in original data file 
#Original
#file_loc = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt'
#Original, permuted
#PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_permuted.txt
#withOTUs, permuted
#PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs_permuted.txt
#Mechanisms file for Subset_PKL script
#/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PentanoicAcid_mechanism_PKL_KG_Triples_Labels.txt
#mechanism_name = 'PentanoicAcid'
#mechanism_name = 'Tryptophan'
#file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/'+mechanism_name+'/Nodes2IntegersPrep/'+mechanism_name+'_mechanism_PKL_KG_Triples_Labels.txt'
#Reduced by Ontologies
#file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_reactome.txt'

#New GutMGene Input
#file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs_withGutMGene.txt'
#file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withOTUs_withGutMGene_withMicrobes.txt'
#file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withGutMGene_withMicrobes.txt'


file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/PKL_v3/PheKnowLator_v3.0.2_full_instance_relationsOnly_OWLNETS_Triples_Identifiers.txt'


with open(file_loc, 'r') as f_in:
    #Length matches original file length
    kg_data = set(tuple(x.split('\t')) for x in f_in.read().splitlines())
f_in.close()

# set output filenames
#Original
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map.json'
#withOTUs, permuted
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_permuted.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withOTUs_permuted.json'
#Original, permuted
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_permuted.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_permuted.json'
#Mechanisms file
#output_ints_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/'+mechanism_name+'/Nodes2IntegersPrep/'+mechanism_name+'_mechanism_PKL_KG_Triples_Integers_node2vecInput.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/'+mechanism_name+'/Nodes2IntegersPrep/'+mechanism_name+'_mechanism_PKL_KG_Triples_Integers_Identifier_Map.json'
#Reduced by Ontologies
#output_ints_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_reactome.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_reactome.json'
#New GutMGene Input
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_withGutMGene.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withOTUs_withGutMGene.json'
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_withGutMGene_withMicrobes.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withOTUs_withGutMGene_withMicrobes.json'
#output_ints_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withGutMGene_withMicrobes.txt'
#output_ints_map_location = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withGutMGene_withMicrobes.json'

output_ints_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/PKL_v3/PheKnowLator_v3.0.2_full_instance_relationsOnly_OWLNETS_Triples_Integers.txt'
output_ints_map_location = '/Users/brooksantangelo/Documents/HunterLab/Exploration/PKL_v3/PheKnowLator_v3.0.2_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map.json'



# map identifiers to integers
entity_map = {}
entity_counter = 0
graph_len = len(kg_data)

ints = open(output_ints_location, 'w', encoding='utf-8')
ints.write('subject' + '\t' + 'predicate' + '\t' + 'object' + '\n')

for s, p, o in tqdm(kg_data):
    subj, pred, obj = s, p, o
    if subj not in entity_map: entity_counter += 1; entity_map[subj] = entity_counter
    if pred not in entity_map: entity_counter += 1; entity_map[pred] = entity_counter
    if obj not in entity_map: entity_counter += 1; entity_map[obj] = entity_counter
    ints.write('%d' % entity_map[subj] + '\t' + '%d' % entity_map[pred] + '\t' + '%d' % entity_map[obj] + '\n')
ints.close()

#write out the identifier-integer map
with open(output_ints_map_location, 'w') as file_name:
    json.dump(entity_map, file_name)



# read original data file and convert 3 columns to 2 (just subjects and objects)
#Original
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput.txt'
#withOTUs, permuted
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_permuted.txt'
#Original, permuted
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_permuted.txt'
#Mechanisms File
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/'+mechanism_name+'/Nodes2IntegersPrep/'+mechanism_name+'_mechanism_PKL_KG_Triples_Integers_node2vecInput.txt'
#Reduced by Ontologies
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_reactome.txt'
#New gutMGene input
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_withGutMGene.txt'
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withOTUs_withGutMGene_withMicrobes.txt'
#inputs_ints_file_loc = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_withGutMGene_withMicrobes.txt'


inputs_ints_file_loc = '/Users/brooksantangelo/Documents/HunterLab/Exploration/PKL_v3/PheKnowLator_v3.0.2_full_instance_relationsOnly_OWLNETS_Triples_Integers.txt'


with open(inputs_ints_file_loc) as f_in:
    kg_data = [x.split('\t')[0::2] for x in f_in.read().splitlines()]
f_in.close()

# write out cleaned file
#Original
#file_out = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned.txt'
#withOTUs, permuted
#file_out = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_withOTUs_permuted.txt'
#Original, permuted
#file_out = '/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Output/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_permuted.txt'
#Mechanisms File
#file_out = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/'+mechanism_name+'/Nodes2IntegersPrep/'+mechanism_name+'_mechanism_PKL_KG_Triples_Integers_node2vecInput_cleaned.txt'
#Reduced by Ontologies
#file_out = '/Users/brooksantangelo/Documents/HunterLab/Exploration/Mechanisms/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_reactome.txt'
#New GutMGene Input
#file_out = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_withOTUs_withGutMGene.txt'
#file_out = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integers_node2vecInput_cleaned_withGutMGene_withMicrobes.txt'


file_out = '/Users/brooksantangelo/Documents/HunterLab/Exploration/PKL_v3/PheKnowLator_v3.0.2_full_instance_relationsOnly_OWLNETS_Triples_node2vecInput_cleaned.txt'


with open(file_out, 'w') as f_out:
    for x in kg_data[1:]:
        f_out.write(x[0] + ' ' + x[1] + '\n')

f_out.close()