import pandas as pd
import os
os.chdir("/Users/yangpei/YangPei/File/Python")
Input_data = pd.read_excel('Input/kegg背景2.xlsx', sheet_name=0)

top10 = Input_data.head(10)
grouped = top10.groupby('gene_id')
result = grouped['pathway']
for a, b in result:
    print(a)
    print(b)



