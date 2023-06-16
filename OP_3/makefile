all: 
	clear 
	# python GEO_datasets/create_dataset.py 
	# python pipeline_sle.py 
	python feature_selection.py 

demo: 
	# pip3 install -r requirements.txt
	# python3 pipeline_plant_ds.py 

top_targets: 
	python top_k_regulators_and_regulated_genes.py --regulator_tf=1 --regulated_target=0 --gene=ELF1 --top_k=20

top_tf: 
	python top_k_regulators_and_regulated_genes.py --regulator_tf=0 --regulated_target=1 --gene=ELF1 --top_k=20


top_all: 
	clear 
	python all_top_k_regulators_and_regulated.py --top_k=20 
	