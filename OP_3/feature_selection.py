import pandas as pd 

""" 
File names to read or write data 
"""
# read current features/transcription_factors here 
tf_names_file = './Datasets/GSE121239/tf_names.tsv'


# write selected_features/transcription_factors here 
selected_features_file = './Datasets/GSE121239/tf_names_selected_features.tsv'

# read results from here 
results_file = './output/GSE121239_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes100_numtfs17/Ranked_list_TF_gene_best_model.csv' 

# Target gene ID: important risk loci: SYNGR1 
target_gene_id = '204287_PM_at' 

# number of features/transcription_factors to select 
with open(tf_names_file) as f:
    lines = f.readlines() 

num_selected_features = int(len(lines)/2) 

# Temporary 
num_selected_features = 10  

results = pd.read_csv(results_file) 
# results 

selected_features = list(results[results['Target']==target_gene_id].sort_values(by='Importance', ignore_index=True).iloc[:num_selected_features]['TF']) 
"""
TODO: Need to check if key genes are present in these selected_features/transcription_factors or not 
"""
"""
Write selected_features/transcription_factors here 
"""

with open(selected_features_file, 'w') as fp:
    for item in selected_features:
        # write each item on a new line 
        fp.write("%s\n" % item) 
