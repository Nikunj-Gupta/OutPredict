import pandas as pd, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--regulated_target", type=int, default=0)
parser.add_argument("--regulator_tf", type=int, default=1)
parser.add_argument("--gene", type=str, default="ELF1")
parser.add_argument("--top_k", type=int, default=10)
args = parser.parse_args()

REGULATED_TARGET = args.regulated_target 
REGULATOR_TF = args.regulator_tf 

GENE = args.gene 
TOP_K = args.top_k 

df = pd.read_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/_parsed_Ranked_list_TF_gene_best_model.csv") 

if REGULATOR_TF:
    file_name = "_".join(["top", str(TOP_K), "genes", "regulated", "by", GENE+".csv"]) 
    df[df["TF.Gene.Symbol"]==GENE].sort_values(by=["Importance"], ascending=False).dropna().iloc[:TOP_K].to_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/top_k_regulators_and_regulated_genes/"+file_name, index=False)
    
if REGULATED_TARGET:
    file_name = "_".join(["top", str(TOP_K), "genes", "that", "regulate", GENE+".csv"]) 
    df[df["Target.Gene.Symbol"]==GENE].sort_values(by=["Importance"], ascending=False).dropna().iloc[:TOP_K].to_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/top_k_regulators_and_regulated_genes/"+file_name, index=False) 

