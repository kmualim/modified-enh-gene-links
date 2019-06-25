# Modified enhancer gene links 

1. Get flanked regions 
- get surrounding region of peaks

```
python get_flanked.py 
-i Neighborhoods/GeneList.TSS1kb.bed 
-g /mnt/lab_data/akundaje/kmualim/ABC-Enhancer-Gene-Prediction/input_data/hg19/hg19.chrom.sizes 
-o . 
-b epi/ENCFF030DCL.bam 
-a epi/ENCFF384ZZM.bam

```
where -i bed file to get flanked regions from 
-g genome file 
-o outdir 
-b DHS bamfile
-a H3K27ac bamfile


2. Get p values for peaks 
```
python get_p_val.py 
-o Neighborhoods/CountReads/Enhancers.DHS.ENCFF030DCL.bam.CountReads.bed 
-a Neighborhoods/CountReads/Enhancers.H3K27ac.ENCFF384ZZM.bam.CountReads.bed
-f flanked.Enhancers.ENCFF030DCL.counts.bed 
-p flanked.Enhancers.ENCFF384ZZM.counts.bed

```
where -o DHS.CountReads.bed file 
-a H3K27ac.CountReads.bed file 
-f flanked.DHS.counts.bed
-p flanked.H3K27ac.counts.bed 

