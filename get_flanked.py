#! bin/bash 
from subprocess import Popen
from subprocess import PIPE
import os.path
import numpy as np 
import pandas as pd 
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--infile', '-i',
		required=True, 
		help='''Target bed file where counts to be computed''')

parser.add_argument('--genome', '-g', 
		required=True, 
		help='''Genome file''')
parser.add_argument('--outdir', '-o', 
		required=True, 
		help='''Outdir''')
parser.add_argument('--slop', '-s', 
		default='5.0', 
		help='''Slop ''')

parser.add_argument('--bamfile', '-b',
		required=True, 
		help=''' DHS/ATAC bam file to get peaks from''')

parser.add_argument('--accessibility', '-a',
		required=True, 
		help=''' h3k27ac bam file to get peaks from''')
args=parser.parse_args()

def get_flanked_regions(infile, outdir, slop, genome, bamfile, accessfile):
        outfile= os.path.join("flanked."+os.path.basename(infile))
        command= "slopBed -pct -l {} -r {} -i {} -g {} > {}".format(slop, slop, infile, genome, outfile)

        print("Running: {}".format(command)) 
        p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        (stdoutdata, stderrdata) = p.communicate()
        err = str(stderrdata, 'utf-8')
        print(err)
	
        h3k27ac_outfile=os.path.join(os.path.basename(outfile) + os.path.basename(bamfile) + ".counts.bed")
        get_H3K27ac_command= "bedtools coverage -g /mnt/lab_data/akundaje/kmualim/ABC-Enhancer-Gene-Prediction/input_data/hg19/hg19.chrom.sizes -counts -a {} -b {} | awk -v OFS='\t' -v FS='\t' '{{print $1, $2, $3, $NF}}' > {}".format(outfile, bamfile, h3k27ac_outfile)
        print("Running: {}".format(get_H3K27ac_command))
        p = Popen(get_H3K27ac_command, stdout=PIPE, stderr=PIPE, shell=True)
        (stdoutdata, stderrdata) = p.communicate()
        err = str(stderrdata, 'utf-8')
        print(err)
	
        dhs_outfile = os.path.join(os.path.basename(outfile) + os.path.basename(accessfile) + ".counts.bed")
        get_DHS_command="bedtools coverage -g /mnt/lab_data/akundaje/kmualim/ABC-Enhancer-Gene-Prediction/input_data/hg19/hg19.chrom.sizes -counts -a {} -b {} | awk -v OFS='\t' -v FS='\t' '{{print $1, $2, $3, $NF}}' > {}".format(outfile, accessfile, dhs_outfile)

        print("Running: {}".format(get_DHS_command))
        p = Popen(get_DHS_command, stdout=PIPE, stderr=PIPE, shell=True)
        (stdoutdata, stderrdata) = p.communicate()
        err = str(stderrdata, 'utf-8')
        print(err)

	#return h3k27ac_outfile, dhs_outfile

get_flanked_regions(args.infile, args.outdir, args.slop, args.genome, args.bamfile, args.accessibility)
