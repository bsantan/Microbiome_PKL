import numpy
import pandas as pd
import argparse

#Define arguments for each required and optional input
def defineArguments():
    parser=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    #parser.add_argument("--otu-curie",dest="otu_curie",required=False,help="otu_curie")
    #parser.add_argument("--disease-curie",dest="disease_curie",required=False,help="disease_curie")

    return parser

###Read in all files
def process_files(triples_file,uri_labels_types_file,labels_file):
    
    #####Load input data
    with open(triples_file, 'r') as f_in:
        triples = set(tuple(x.split('\t')) for x in f_in.read().splitlines())
    f_in.close()

    triples_list = list(triples)

    uri_labels = pd.read_csv(uri_labels_types_file,sep=',')

    labels = {}

    with open(labels_file) as f_in:
        for line in f_in:
            vals = line.strip().split("\t")
            try:
                key, value = vals[2:4]
                labels[key] = value
            except: pass

    return triples_list,uri_labels,labels


def generate_contextual_labels(triples_list,uri_labels,labels):

    #Create dict of all PKL hashes and their labels according to the microbe they represent
    microbes_contextual = pd.DataFrame(columns = ['Identifier','Label'])

    for i in range(len(triples_list)):
        s = triples_list[i][0]
        p = triples_list[i][1]
        #Based on patterns added from OWL-NETS, contextual microbe with PKL hash is always a subclass of NCBITaxon, so NCBITaxon will be the object
        o = triples_list[i][2]
        try:
            o_type = uri_labels.loc[uri_labels['Identifier'] == o,'Type'].values[0]
            #print(s,'    ',p,'    ',o)
        except: 
            continue

        #Only find relevant contextual microbes, which are PKL hashes
        if o_type == 'microbe' and 'pkt/' in s and '#subClassOf' in p:
            d = {}
            microbe_label = uri_labels.loc[uri_labels['Identifier'] == o,'Label'].values[0]
            d['Identifier'] = s
            d['Label'] = 'CONTEXTUAL ' + microbe_label
            microbes_contextual = microbes_contextual.append(d,ignore_index=True)
        

    #Get contextual entities in another loop
    #STEP 1: Add UBERON context
    for i in range(len(triples_list)):
        s = triples_list[i][0]
        p = triples_list[i][1]
        o = triples_list[i][2]
        #Based on patterns added from OWL-NETS, location of microbe for context will be UBERON or NCBITaxon with located in as relationship
        if 'pkt/' in s and p == '<http://purl.obolibrary.org/obo/RO_0001025>' and 'UBERON' in o:
            #try:
            microbe_label = microbes_contextual.loc[microbes_contextual['Identifier'] == s,'Label'].iloc[0]
            #except IndexError:
            #print(microbe_label)
            contextual_label = microbe_label + ": " + labels[o]
            #Update microbes_contextual df
            microbes_contextual.loc[microbes_contextual['Identifier'] == s,'Label'] = contextual_label

    #Need to change the mouse label since it is in another language
    labels['<http://purl.obolibrary.org/obo/NCBITaxon_10090>'] = 'Mus musculus'

    #STEP 2: Add organism context
    for i in range(len(triples_list)):
        s = triples_list[i][0]
        p = triples_list[i][1]
        o = triples_list[i][2]
        #Based on patterns added from OWL-NETS, location of microbe for context will be UBERON or NCBITaxon with located in as relationship
        if p == '<http://purl.obolibrary.org/obo/RO_0001025>' and 'NCBITaxon' in o:
            microbe_label = microbes_contextual.loc[microbes_contextual['Identifier'] == s,'Label'].iloc[0]
            contextual_label = microbe_label + " " + labels[o]
            #Update microbes_contextual df
            microbes_contextual.loc[microbes_contextual['Identifier'] == s,'Label'] = contextual_label

    return microbes_contextual

def output_labels_file(microbes_contextual,output_dir):

    microbes_contextual.to_csv(output_dir + '/gutMGene_microbes_contextual_labels.csv', index = False)

def combine_labels_files(microbes_contextual,uri_labels,output_dir):

    #uri_labels_new = pd.DataFrame(columns = ['Identifier','CURIE','Label','Type'])

    for i in range(len(microbes_contextual)):
        d = {}
        d['Identifier'] = microbes_contextual.iloc[i].loc['Identifier']
        d['CURIE'] = 'none'
        d['Label'] = microbes_contextual.iloc[i].loc['Label']
        d['Type'] = 'microbe'
        uri_labels = uri_labels.append(d,ignore_index=True)

    uri_labels.to_csv(output_dir + '/LabelTypes_gutMGene_URI_LABEL_MAP_contextual.csv', index = False)

######

def main():

    #Define Inputs
    triples_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples_Brackets.txt"

    labels_file = "/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_NodeLabels.txt"

    uri_labels_types_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/LabelTypes_gutMGene_URI_LABEL_MAP_withTaxa.csv"

    output_dir = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene"
   
    #Generate argument parser and define arguments
    parser = defineArguments()
    args = parser.parse_args()

    #Algorithm
    triples_list,uri_labels,labels = process_files(triples_file,uri_labels_types_file,labels_file)

    microbes_contextual = generate_contextual_labels(triples_list,uri_labels,labels)

    output_labels_file(microbes_contextual,output_dir)

    combine_labels_files(microbes_contextual,uri_labels,output_dir)

if __name__ == '__main__':
    main()    
