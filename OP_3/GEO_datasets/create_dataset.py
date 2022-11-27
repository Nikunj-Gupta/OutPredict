""" 
Inputs: 
1. gene_expressions_dataset     : all gene expressions dataset 
2. top_k_genes                  : de or Coefficient of variation; must have gene ids and gene symbols 
3. gene_symbol_mapping          : mapping dictionary from gene symbols to IDs used in datasets; optional as of now 
4. human_TFs                    : List of human TFs (from University of Toronto) 


Outputs: 
1. expression.tsv 
2. tf_names.tsv 
3. metadata.tsv 

""" 

import pandas as pd, os 

SAVE = True 

gene_expressions_dataset_file = './GEO_datasets/GSE121239/log2_expre.csv'

top_k_genes_file = './GEO_datasets/GSE121239/top_k_de_genes_file.tsv' 

gene_symbol_mapping = {
    'ELF1': '212420_PM_at', 
    'IRF1': '202531_PM_at', 
    'SYNGR1': '204287_PM_at', 
    'PTBRB': None, 
    'UNC5A': '236448_PM_at', 
    'MT1F': '217165_PM_x_at' 
}

human_TFs_file = './GEO_datasets/human_TFs/DatabaseExtract_v_1.01.csv'

expression_tsv_file = './Datasets/GSE121239/expression.tsv' 

tf_names_tsv_file = './Datasets/GSE121239/tf_names.tsv' 

metadata_tsv_file = './Datasets/GSE121239/meta_data.tsv' 


gene_expressions_dataset = pd.read_csv(gene_expressions_dataset_file) 

top_k_genes = pd.read_csv(top_k_genes_file, sep='\t') 
# Temporary 
top_k_genes = top_k_genes.iloc[:5000] 

"""
expression.tsv
"""

expression = gene_expressions_dataset.loc[gene_expressions_dataset['Unnamed: 0'].isin(top_k_genes['ID'])] 
"""

Matching human TFs 
"""

human_TFs = pd.read_csv(human_TFs_file) 
matching_TFs = list(set(human_TFs['HGNC symbol']) & set(top_k_genes['Gene.symbol'].dropna())) 

list_of_human_TFs = top_k_genes.loc[top_k_genes['Gene.symbol'].isin(pd.Series(matching_TFs))]['ID']  

"""
Metadata for the case where all datapoints are considered Steady State 
"""

metadata = pd.DataFrame(columns=['isTs', 'is1stLast', 'prevCol', 'del.t', 'condName']) 
metadata['condName'] = list(expression.columns[2:]) 
metadata['isTs'] = "FALSE" 
metadata['is1stLast'] = "e" 
metadata['prevCol'] = "NA" 
metadata['del.t'] = "NA" 
metadata 

if SAVE: 
    path = os.path.dirname(os.path.realpath(expression_tsv_file)) 
    if not os.path.exists(path): 
        os.makedirs(path)
    expression.to_csv(expression_tsv_file, sep="\t", index=False) 
    list_of_human_TFs.to_csv(tf_names_tsv_file, sep="\n", index=False, header=False) 
    metadata.to_csv(metadata_tsv_file, sep="\t", index=False) 
    print('Saved!') 