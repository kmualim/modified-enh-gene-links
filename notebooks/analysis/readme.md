# Notebooks in this repository: 

The two notebooks I'll point your attention to is : 

<b>data_exploration_abc_all.ipynb</b>	: this notebook details data exploration on the ABC weighted neural network embeddings (extracted from the Basset 2016 paper)
-- looks into understanding why the model is having trouble fitting this data 
-- characteristics of the data


<b>initial_models_abc_all.ipynb</b>	: this notebook details the initial models applied to the ABC weighted neural network embeddings (extracted from the Basset 2016 Paper)
-- looks into models used and analysis of the models 
-- performance of the models 

<b> varying_inputs.ipynb</b> : this notebook details the how varying inputs alters the correlation coefficient. 
Inputs tried : 
1. JUST promoter sequences * promoter scores 
2. JUST using enhancer-gene linking scores 

### Data paths for PROCESSED datasets:

Ground Truth labels have the following format: 
Gene "\t" Expression(TPM) "\t" True Label 
True Label : 1 if TPM > 1 else 0

Regression datasets for just expressed genes: 
/mnt/lab_data2/kmualim/Jamboree_data/notebooks/datasets/7580_abc_large_expressed_labels.npz :(7580, 1)
/mnt/lab_data2/kmualim/Jamboree_data/notebooks/datasets/7580_abc_large_expressed.npz : (7580,1000)

Regression datasets (ABC.Score + nn embeddings): 
/mnt/lab_data2/kmualim/Jamboree_data/notebooks/datasets/train_valid_test_all/: 
train_gene_labels_reg_all.npz 
test_gene_labels_reg_all.npz 
valid_gene_labels_reg_all.npz : where gene_labels_reg represent the corresponding gene names

Labels after logistic regression classification (accuracy ~0.7 across train, valid, test sets): 
/mnt/lab_data2/kmualim/Jamboree_data/notebooks/datasets/*_classification_labels_abc_large.npz : (16525, 1)

### How were embeddings obtained ? 
1. Enhancer regions for each gene was determined by running the ABC code to generate ABC Scores 
2. EnhancerPredictions.txt file from the output of ABC was passed through `make_enhancer_regions.py` that extends each enhancer feature to 1000bp and appends promoter sequence regions 
3. Using the output of `make_enhancer_regions.py` : pass corresponding bed file into locusselect code to extract embeddings from Basset 2016 Classification model 
4. Multiply corresponding embeddings with ABC.Score for each enhancer gene link
5. Add all the sequence embeddings for each gene to generate final gene-by-sequence-embeddings matrix shape=(k genes * 1000)

### Data paths : 

ABC.Score for corresponding enhancer + promoter regions :
-- files obtained after passing through `make_enhancer_regions.py`
/mnt/lab_data2/kmualim/Jamboree_data/enh_gene_links/enh_gene_dist_*.bed : (6532980, 5)
where 5 columns represent : (chr, start, end, ABC Score, TargetGene) 

/mnt/lab_data2/kmualim/Jamboree_data/enh_gene_links/k562_dnase_all_putative_classification_embeddings.0.-3.npz
-- corresponding sequence embeddings to enh_gene_dist_*.bed 


