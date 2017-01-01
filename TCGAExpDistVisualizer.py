# -*- coding: utf-8 -*-
# Making boxplot that describes the expression of your gene-of-interest in primary tumor and normal tissue from TCGA datasets.

import pandas as pd
import matplotlib.pyplot as plt


def load(genomic_matrix, clinical_data):
    try:
        _gdata = pd.read_csv(genomic_matrix, delimiter='\t', index_col=0)
        _cdata = pd.read_csv(clinical_data, delimiter='\t', index_col=0)
    except:
        raise OSError('File is not found')

    gdata = _gdata.T
    cdata = _cdata['sample_type']
    return gdata, cdata


def aligndata(gdata, cdata, genename):
    picked_gdata = gdata[genename]
    eval_df = pd.concat([cdata, picked_gdata], axis=1, join='inner')
    return eval_df


def show_or_save_chart(eval_df, genename):

    bp = eval_df.boxplot(column=genename, by='sample_type')
    bp.plot()

    savename = genename + '.png'

    plt.savefig(savename)
    print('Saved as' + savename)

    return


def main(gdata, cdata):
    genelist = list(gdata.T.index)

    print('Please enter your gene of interest.')
    genename = input('>>')

    if genename not in genelist:
        print('your GOI is not found')
        return

    eval_df = aligndata(gdata, cdata, genename)
    show_or_save_chart(eval_df, genename)


if __name__ == '__main__':
    endflg = False

    print("Loading...")
    gdata, cdata = load("genomicMatrix", "clinical_data")

    while not endflg:
        main(gdata, cdata)
        endflg = input('Quit? [y/n]') == 'y'

    print("Quit")
