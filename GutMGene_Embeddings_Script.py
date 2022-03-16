# import needed libraries
import datetime
import glob
import ijson
import itertools
import networkx
import numpy
import pandas as pd
import pickle
import requests
import json
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import random
import statistics
import math
import copy
import numpy as np
from collections import defaultdict
from scipy import spatial
from scipy.spatial import distance
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv 
from matplotlib.collections import LineCollection
from sklearn.decomposition import PCA
import argparse
from tqdm import tqdm


#Define arguments for each required and optional input
def defineArguments():
    parser=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    return parser

###Read in all files
def process_files(embeddings_file,identifier_json,labels_file,pca_labels_file):
    #####Load input data
    f = open(identifier_json)
    iden = json.load(f)

    ##Embeddings data
    emb = KeyedVectors.load_word2vec_format(embeddings_file, binary=False)

    labels = {}

    with open(labels_file) as f_in:
        for line in f_in:
            vals = line.strip().split("\t")
            try:
                key, value = vals[2:4]
                labels[key] = value
            except: pass

    pca_labels = pd.read_csv(pca_labels_file,sep=',')

    return iden,emb,labels,pca_labels

######

#######Load in ontologies

#Create dictionary of all metadata by entity URLs
def entity_representation_urls(uri_labels_types_file,entity_IDs):

    uri_labels = pd.read_csv(uri_labels_types_file,sep=',')

    for i in range(len(uri_labels)):
        label = uri_labels.iloc[i].loc['Label']
        #if uri_labels.iloc[i].loc['Type'] == 'microbe':
        #Interested in CONTEXTUAL microbes as nodes
        if uri_labels.iloc[i].loc['Type'] == 'microbe' and 'CONTEXTUAL' in label:
            entity_IDs[label] = uri_labels.loc[uri_labels['Label'] == label, 'Identifier'].values[0]

    #Remove keys with empty values- probably not necessary   
    {k: v for k, v in entity_IDs.items() if v is not None}

    print(len(entity_IDs))

    return entity_IDs

#Add dictionary for processes of interest
def entity_representation_urls_comparison(processes_of_interest_file,entity_IDs_comparison):

    uri_labels = pd.read_csv(processes_of_interest_file,sep=',')

    for i in range(len(uri_labels)):
        label = uri_labels.iloc[i].loc['Label']
        entity_IDs_comparison[label] = uri_labels.loc[uri_labels['Label'] == label, 'Identifier'].values[0]

    #Remove keys with empty values- probably not necessary     
    {k: v for k, v in entity_IDs_comparison.items() if v is not None}

    return entity_IDs_comparison

#Get GO and MONDO processes
def get_embeddings(iden,emb,labels,output_dir):

    #diseases = [items for key,val in iden.items() if 'MONDO_' in key]
    #processes = [key for key,val in iden.items() if 'GO_' in key]

    diseases = dict(filter(lambda item: 'MONDO_' in item[0], iden.items()))
    processes = dict(filter(lambda item: 'GO_' in item[0], iden.items()))

    dfs = []

    for l in [diseases,processes]:
        #Initialize dictionaries for otu embeddings
        embeddings = defaultdict(list)
        for ontology,embed in l.items():
            embedding_array = emb[str(embed)]
            embedding_array = np.array(embedding_array)
            #Get name based on url
            label = labels[ontology]
            embeddings[label] = embedding_array

        embeddings_df = pd.DataFrame.from_dict(embeddings, orient='index')
        dfs.append(embeddings_df)

    dfs[0].to_csv(output_dir+'/MONDO_embeddings_df.csv')
    dfs[1].to_csv(output_dir+'/GO_embeddings_df.csv')

    return dfs[0],dfs[1]

#######

######Represent all OTUs and immune entities as vectors of embeddings 
def generate_vector_embeddings(iden,emb,entity_IDs,output_dir,output_filename):

    used_columns = entity_IDs.keys()

    #Initialize dictionaries for otu embeddings
    embeddings = defaultdict(list)

    for column in used_columns:
        #Get the ontology URL for the corresponding column
        ontology = entity_IDs[column]
        embed = str(iden.get(ontology))
        #Handle microbes that did not have any relationships in GutMGene but were added to KG (i.e. Clostridium sporogenes Ll.LtrB-eryR)
        try:
            embedding_array = emb[embed]
            embedding_array = np.array(embedding_array)
            embeddings[column] = embedding_array
        except: KeyError
        pass 

    embeddings_df = pd.DataFrame.from_dict(embeddings, orient='index')
    embeddings_df.to_csv(output_dir+output_filename)

    return embeddings_df

##### Visualize clusters

##PCA
def perform_pca(otu_embeddings_df,pca_labels,output_dir):

    import plotly.express as px

    otu_embeddings_pca = copy.deepcopy(otu_embeddings_df)

    otu_embeddings_pca.reset_index(drop=True, inplace=True)

    PCA_func = PCA(n_components=4)
    pca_embedding = PCA_func.fit_transform(otu_embeddings_pca)

    x_varexp = round(PCA_func.explained_variance_ratio_[0] * 100,2)
    y_varexp = round(PCA_func.explained_variance_ratio_[1] * 100,2)
    th_varexp = round(PCA_func.explained_variance_ratio_[2] * 100,2)
    fo_varexp = round(PCA_func.explained_variance_ratio_[3] * 100,2)

    pca_embedding = pd.DataFrame(pca_embedding, columns = ['Dim1 ('+str(x_varexp)+'%)','Dim2 ('+str(y_varexp)+'%)','Dim3 ('+str(th_varexp)+'%)','Dim4 ('+str(fo_varexp)+'%)'])


    '''
    for i in range(len(pca_labels)):
        if pca_labels.iloc[i].loc['Label'] not in otu_embeddings_df.index:
            remove = pca_labels.iloc[i].loc['Label']

    pca_labels = pca_labels[pca_labels['Label'] != remove]

    '''

    pca_labels = pca_labels.drop_duplicates(subset=['Label'])

    print(len(pca_labels))
    print(len(list(otu_embeddings_df.iloc[:,0])))
    print(otu_embeddings_df.columns)
    print(otu_embeddings_df.index.tolist())

    for i in list(pca_labels['Label']):
        if i not in otu_embeddings_df.index.tolist():
            print('not in otu_embeddings ',i)

    fig = px.scatter(pca_embedding, x=pca_embedding.columns[0], y=pca_embedding.columns[1],color=pca_labels['Property'])
    #Include in px.scatter command for coloring microbes by property, ie for butyrate producer
    #color=pca_labels['Property']
    fig.update_layout(title_text='PCA of OTU Embeddings', title_x=0.5)
    fig.write_image(output_dir+"/PCA_embeddings_otus.png")


#Use embeddings from all data as input to calc cosine dist to a given set of diseases and processes
def calc_cosine_dist(otu_embeddings_df,comp_embeddings_df,output_dir,output_filename):

    otus = list(otu_embeddings_df.index)
    entities = list(comp_embeddings_df.index)

    #Confused why my manual math of cosine similarity yields the same result as 1-spatial.distance.cosine(a,b) here, should be 1-(CosineSimilarity)?
    cosine_similarities_otus = pd.DataFrame(columns = ['microbe']+entities)

    #Calculate cosine distance between each otu and comparison embeddings
    for i in tqdm(range(len(otus))):
        d = {}
        d['microbe'] = otus[i]
        for j in range(len(entities)):
            d[entities[j]] = 1 - spatial.distance.cosine(list(otu_embeddings_df.iloc[i]),list(comp_embeddings_df.iloc[j]))
        cosine_similarities_otus = cosine_similarities_otus.append(d,ignore_index=True)

    cosine_similarities_otus.to_csv(output_dir+output_filename, index = False)

    return cosine_similarities_otus

def calc_max_cosine_dist(cosine_similarities_otus,output_dir,output_filename):

    max_cosine = pd.DataFrame(columns=['Entity','OTU','Cosine Distance'])

    #Get closest microbes to each process of interest
    for i in cosine_similarities_otus.columns[1:,]:
        d = {}
        d['Entity'] = i
        max_val = cosine_similarities_otus[i].max()
        d['OTU'] = cosine_similarities_otus.loc[cosine_similarities_otus[i] == max_val,'microbe'].values[0]
        d['Cosine Distance'] = max_val
        max_cosine = max_cosine.append(d,ignore_index=True)

    max_cosine.to_csv(output_dir+output_filename, index = False)

def main():

    #Define Inputs
    #42 dimensions with newer assertions - 2/27
    embeddings_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/Node2Vec_DimensionCheck/PheKnowLator_v2_node2vec_Embeddings42_0.emb"

    #With newer assertions - 2/23
    identifier_json = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_Triples_Integer_Identifier_Map_withGutMGene_withMicrobes.json"

    labels_file = "/Users/brooksantangelo/Documents/Rotation2/TiffanyFiles/Node2Vec/Inputs/PheKnowLator_v2.1.0_full_instance_relationsOnly_OWLNETS_NodeLabels.txt"

    #Use contextual labels file
    uri_labels_types_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/LabelTypes_gutMGene_URI_LABEL_MAP_contextual.csv"
    processes_of_interest_file = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/processes_URI_LABEL_MAP.csv"

    pca_labels_file = '/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/GutMGene_ButyrateProducer_Labels.csv'

    output_dir = "/Users/brooksantangelo/Documents/Rotation2/Rocky/PKL_Additions/GutMGene/AnalysisOutput/42DimAssertions"

    #Algorithm
    iden,emb,labels,pca_labels = process_files(embeddings_file,identifier_json,labels_file,pca_labels_file)

    entity_IDs = {}
    entity_IDs_comparison = {}

    entity_IDs = entity_representation_urls(uri_labels_types_file,entity_IDs)
    entity_IDs_comparison = entity_representation_urls_comparison(processes_of_interest_file,entity_IDs_comparison)

    mondo_embeddings_df,go_embeddings_df = get_embeddings(iden,emb,labels,output_dir)

    print('# MONDO Diseases: ',len(mondo_embeddings_df))
    print('# GO Processes: ',len(go_embeddings_df))

    otu_embeddings_df = generate_vector_embeddings(iden,emb,entity_IDs,output_dir,'/otu_embeddings.csv')

    interest_embeddings_df = generate_vector_embeddings(iden,emb,entity_IDs_comparison,output_dir,'/comp_embeddings.csv')

    perform_pca(otu_embeddings_df,pca_labels,output_dir)

    #Get cosine distances to each entity of interest
    processes_of_interest_cosine_sim = calc_cosine_dist(otu_embeddings_df,interest_embeddings_df,output_dir,'/processes_of_interest_cosine_sim.csv')
    calc_max_cosine_dist(processes_of_interest_cosine_sim,output_dir,'/max_cosine_processes_of_interest.csv')

    #This takes ~2.5-3hrs
    print("Calculating Cosine Distance for Mondo Diseases")
    mondo_cosine_sim = calc_cosine_dist(otu_embeddings_df,mondo_embeddings_df,output_dir,'/mondo_cosine_sim.csv')
    calc_max_cosine_dist(mondo_cosine_sim,output_dir,'/max_cosine_mondo.csv')

    print("Calculating Cosine Distance for GO Processes")
    go_cosine_sim = calc_cosine_dist(otu_embeddings_df,go_embeddings_df,output_dir,'/go_cosine_sim.csv')
    calc_max_cosine_dist(go_cosine_sim,output_dir,'/max_cosine_go.csv')

if __name__ == '__main__':
    main()