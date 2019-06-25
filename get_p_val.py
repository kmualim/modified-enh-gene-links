#! bin/bash 
import os
import sys 
import numpy as np
import pandas as pd 
import scipy.stats
import numpy 
import argparse
import collections

parser = argparse.ArgumentParser()
parser.add_argument('--o_dhs', '-o', 
		required=True, 
		help=''' genes dhs count file''')
parser.add_argument('--o_h', '-a', 
		required=True, 
		help=''' genes h3k27ac count file''')
parser.add_argument('--f_dhs', '-f', 
		required=True,
		help=''' flanked genes dhs count file''')
parser.add_argument('--f_h', '-p', 
		required=True, 
		help='''flanked genes h3k27ac count file''')

args = parser.parse_args()

def get_pval_files(o_dhs, o_h, f_dhs, f_h): 
        enh_DHS_counts = pd.read_csv(args.o_dhs, sep='\t', header=None)
        enh_H_counts = pd.read_csv(args.o_h, sep='\t', header=None)
        flank_DHS_counts = pd.read_csv(args.f_dhs, sep='\t', header=None)
        flank_H_counts = pd.read_csv(args.f_h, sep='\t', header=None)
        #print(enh_DHS_counts[:5])
        enh_DHS_counts['length']= enh_DHS_counts[2] - enh_DHS_counts[1]
        #print(enh_DHS_counts['length'][:5])
        flank_DHS_counts['length']= flank_DHS_counts[2]-flank_DHS_counts[1]
        #exit(1)
        ct = {'counts': enh_DHS_counts[3], 'flank_counts': flank_DHS_counts[3], 'flank_length': flank_DHS_counts['length'],'length': enh_DHS_counts['length']}
        #ct = pd.DataFrame(ct_2)
        ct['log10_pval'] = [-1]*len(ct['counts'])
        #print(ct['counts'][:5])
        #print(ct['length'][:5])
        #print(ct[:5])
        for i in range(len(ct['counts'])):
            if (ct['counts'][i] == 0 and ct['flank_counts'][i] == 0) or ct['flank_length'][i] == 0:
                ct['log10_pval'][i]='NA'
            else:
                ct['log10_pval'][i]= -np.log10(scipy.stats.chi2_contingency([[ct['flank_counts'][i], ct['counts'][i]], [ct['flank_length'][i], ct['length'][i]]])[1] + sys.float_info.min)
        #print(ct['log10_pval'][:5])
        pval_counts=os.path.join(os.path.basename(o_dhs)+ ".pvalue.bed")
        data_f = collections.OrderedDict() 
        data_f['chr']= enh_DHS_counts[0]
        data_f[ 'start']= enh_DHS_counts[1]
        data_f['end']= enh_DHS_counts[2]
        data_f[ 'p_value']= ct['log10_pval']
        df = pd.DataFrame(data_f, columns=data_f.keys())
        #print(df[:5])
        df.to_csv(pval_counts, index=False, header=False)
	
        enh_H_counts['length']= enh_H_counts[2] - enh_H_counts[1]
        flank_H_counts['length']= flank_H_counts[2]-flank_H_counts[1]
        ct_1 = {'counts': enh_H_counts[3], 'flank_counts': flank_H_counts[3], 'flank_length': flank_H_counts['length'],'length': enh_H_counts['length']}
        ct_1['log10_pval'] = [-1]*len(ct_1['counts'])

        for i in range(len(ct_1['counts'])-1):
            if (ct_1['counts'][i] == 0 and ct_1['flank_counts'][i] == 0) or ct_1['flank_length'][i] == 0:
                ct_1['log10_pval'][i]='NA'
            else:
                ct_1['log10_pval'][i]= -np.log10(scipy.stats.chi2_contingency([[ct_1['flank_counts'][i], ct_1['counts'][i]], [ct_1['flank_length'][i], ct_1['length'][i]]])[1] + sys.float_info.min)
        data_f = collections.OrderedDict()
        data_f['chr']= enh_H_counts[0]
        data_f['start']= enh_H_counts[1]
        data_f[ 'end']= enh_H_counts[2]
        data_f[ 'p_value']= ct_1['log10_pval']
        pval_counts_1 = os.path.join(os.path.basename(o_h) + ".pvalue.bed")
        df = pd.DataFrame(data_f)
        df.to_csv(pval_counts_1, index=False, header=False)  	

get_pval_files(args.o_dhs, args.o_h, args.f_dhs, args.f_h)





