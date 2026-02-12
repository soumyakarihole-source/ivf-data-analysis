'''
The goal of preprocessing is to clean the dataset, handle missing and inconsistent
 values, standardize formats, and prepare the data for analysis or visualization.
'''

import pandas as pd
import numpy as np

df = pd.read_excel(r'C:/Users/MicroApt/Desktop/3600DigiTMG_Project/Data/DataSet.xlsx')
df.info()
df.shape

# Convert all of them to NaN because Python understands only NaN as missing
df.replace(['N', '-', '_', ' '], np.nan, inplace=True)

# Long / special-character column names cause errors. it will Improves readability and Avoids KeyError
df.rename(columns={
    'Clinical pregnancy: 0:0, Chemical: 1:1 Positive': 'Clinical_pregnancy'
}, inplace=True)



# Convert >20 → 20 (lower-bound clinical standard)
df['PROGESTERONE'] = (
    df['PROGESTERONE']
    .astype(str)
    .str.strip()
    .apply(lambda x: x[1:] if x.startswith('>') else x)
)

df['E2'] = (
    df['E2']
    .astype(str)
    .str.strip()
    .apply(lambda x: x[1:] if x.startswith('>') else x)
)


# Convert Data Types
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['Spouse AGE'] = pd.to_numeric(df['Spouse AGE'], errors='coerce')

# Convert Data Types of binary colums
binary_cols = [
    'Clinical_pregnancy', 'Live Birth',
    'Neonatal Death', 'twin', 'EU'
]

for col in binary_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    

    
# Convert Data Types of Hormonal columns
hormonal_cols = ['BHCG 12', 'BHCG 14', 'FSH', 'AMH', 'E2', 'PROGESTERONE']

for col in hormonal_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    

# Convert Data Types of Procedure / clinical columns
procedure_cols = [
    'NUMBER OF OOCYTES',
    'Embryo Tranfer Day',
    'Number of Embryos Transferred',
    'ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER',
    'IND. NUMBER OF DAYS',
    'WEEK OF BIRTH',
    'ABORTION'
]

for col in procedure_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    

# If BHCG 12 or 14 missing → NULL and If BHCG 12 = 0 → NULL
#Returns NaN if: BHCG 12 missing, BHCG 14 missing, BHCG 12 = 0
df['BHCG_12_14_Percent_Increase'] = np.where(
    (df['BHCG 12'].isna()) |
    (df['BHCG 14'].isna()) |
    (df['BHCG 12'] == 0),
    np.nan,
    ((df['BHCG 14'] - df['BHCG 12']) / df['BHCG 12']) * 100
)

# Remove original Excel-calculated BHCG % column
df.drop(columns=['BHCG 12-14% increase'], inplace=True)

#rename column name
df.rename(columns={
    'BHCG_12_14_Percent_Increase': 'BHCG 12-14% increase'
}, inplace=True)



# Handle Missing Values
df.isna().mean() * 100


# Final Data Validation
df.info()
df.describe(include='all')


# Save Clean Dataset
df.to_excel("IVF_Cleaned_Dataset.xlsx", index=False)

#checking any N, -, _, empty strings left
(df == 'N').sum().sum()
(df == '-').sum().sum()
(df == '<20').sum().sum()
df.head()

for col in df.columns:
    print(col)
    
import os
os.getcwd()

os.chdir(r"C:\Users\MicroApt\Desktop\3600DigiTMG_Project\Data\EDA")

