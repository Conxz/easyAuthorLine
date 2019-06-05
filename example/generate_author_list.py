import pandas as pd
import numpy as np

dat_file = '..\doc\draft_Authorlist_AsymmetryOCD_v2.xlsx'
#dat = pd.read_excel(dat_file,'full co authors')#'full co authors') #'full consortium')
dat = pd.read_excel(dat_file,'full consortium')#'full co authors') #'full consortium')
affiliation_cols = ['Affiliation1','Affiliation2','Affiliation3','Affiliation4','Affiliation5']
affiliations = []
authors = []

affi_j = 1
for i, author in enumerate(dat['Name']):
    author_affi_list = []
    for affi in affiliation_cols:
        if not pd.isnull(dat[affi][i]):
            if dat[affi][i] in affiliations:
                affi_index = affiliations.index(dat[affi][i])+1
            else:
                affiliations.append(dat[affi][i])
                affi_index = affiliations.index(dat[affi][i])+1
            author_affi_list.append(str(affi_index))
        else:
            break
    #print author, author_affi_list
    authors.append(author+' ('+','.join(author_affi_list)+')')

author_list_str = ', '.join(authors)
print author_list_str

affi_lines = []
for i, affi in enumerate(affiliations):
    print str(i+1)+'.', affi+'.'
    affi_lines.append(str(i+1)+'. ' + affi)

# acknowledgement & disclosure
akc_col = 'Acknowledgements'
author_ack_str = []
dis_col = 'Disclosures'
author_dis_str = []
for i, author in enumerate(dat['Name']):
    if not pd.isnull(dat[akc_col][i]):
        author_ack_str.append(author+' was supported by '+ dat[akc_col][i])
    if not pd.isnull(dat[dis_col][i]):
        author_dis_str.append(author+': '+ dat[dis_col][i])

#akc_list_str = '\n'.join(author_ack_str)
#dis_list_str = '\n'.join(author_dis_str)
akc_list_str = '; '.join(author_ack_str)
dis_list_str = '; '.join(author_dis_str)

print akc_col
print akc_list_str
print dis_col
print dis_list_str

affi_line = '; '.join(affi_lines)
print affi_line