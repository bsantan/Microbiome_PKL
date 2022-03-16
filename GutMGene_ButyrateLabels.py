import argparse
import pandas as pd

###Read in all files
def process_files(triples_file,uri_labels_file):
    
    #####Load input data

    with open(triples_file, 'r') as f_in:
        triples = set(tuple(x.split('\t')) for x in f_in.read().splitlines())
    f_in.close()

    triples_list = list(triples)

    uri_labels = pd.read_csv(uri_labels_file,sep=',')

    return triples_list,uri_labels

######

def subset_triples(triples_list,uri_labels,output_dir,output_filename):

    uri_label = uri_labels.loc[uri_labels['Label'] == 'butyrate','Identifier'].values[0]

    #Get all triples of butyrate from the relvant GutMGene triples
    butyrate_triples = list(set(list(filter(lambda triples_list: uri_label in triples_list[2], triples_list))))

    #Get all contextual microbes that are related to butyrate
    butyrate_microbes = []

    for i in range(len(butyrate_triples)):
        contextual_microbe = uri_labels.loc[uri_labels['Identifier'] == butyrate_triples[i][0],'Label'].values[0]
        #If interested in non-contextual microbes
        #butyrate_microbes.append(contextual_microbe.split('CONTEXTUAL ')[1])
        #If interested in contextual microbes
        butyrate_microbes.append(contextual_microbe)

    microbe_properties = pd.DataFrame(columns = ['Label','Property'])

    #Subset only OTUs from labels
    otus = uri_labels.loc[uri_labels['Type'] == 'microbe']
    otus.reset_index(drop=True, inplace=True)

    for i in range(len(otus)):
        d = {}
        label = otus.iloc[i].loc['Label']
        if 'CONTEXTUAL ' in label:
            if label in butyrate_microbes:
                d['Label'] = label
                d['Property'] = 'butyrate'
            #Account for all other contextual microbes
            elif label not in butyrate_microbes:
                d['Label'] = label
                d['Property'] = 'none'
            microbe_properties = microbe_properties.append(d,ignore_index=True)


    microbe_properties.to_csv(output_dir+output_filename, index = False)

def main():

    #2/23 file
    #triples_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Identifiers_withGutMGene_withMicrobes.txt"

    #2/23 GutMGene triples only
    triples_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/gutMGene_OWLNETS_Triples_Brackets.txt"

    #2/23 file that includes labels for contextual microbes
    uri_labels_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/LabelTypes_gutMGene_URI_LABEL_MAP_contextual.csv"
    
    ##Update according to analysis type
    output_dir = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene"

    triples_list,uri_labels = process_files(triples_file,uri_labels_file)

    subset_triples(triples_list,uri_labels,output_dir,'/GutMGene_ButyrateProducer_Labels.csv')

if __name__ == '__main__':
    main()