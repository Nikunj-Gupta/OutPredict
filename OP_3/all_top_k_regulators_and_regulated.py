import pandas as pd, argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--top_k", type=int, default=10)
args = parser.parse_args()


TOP_K = args.top_k 

df = pd.read_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/_parsed_Ranked_list_TF_gene_best_model.csv") 
tfs = set(df["TF.Gene.Symbol"]) 
targets = set(df["Target.Gene.Symbol"].dropna(how='all')) 

for tf in tfs: 
    print(tf)
    file_name = "_".join(["top", str(TOP_K), "targets", "regulated", "by", tf+".csv"]) 
    df[df["TF.Gene.Symbol"]==tf].sort_values(by=["Importance"], ascending=False).dropna().iloc[:TOP_K].to_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/top_k_regulators_and_regulated_genes/"+file_name, index=False)

for target in targets: 
    print(target) 
    file_name = "_".join(["top", str(TOP_K), "TFs", "that", "regulate", target+".csv"]) 
    df[df["Target.Gene.Symbol"]==target].sort_values(by=["Importance"], ascending=False).dropna().iloc[:TOP_K].to_csv("output/GSE65391_output_RF_Ksqrt_ntrees300_datatypeSS_LOdataSS_numgenes5000_numtfs656/top_k_regulators_and_regulated_genes/"+file_name, index=False) 

