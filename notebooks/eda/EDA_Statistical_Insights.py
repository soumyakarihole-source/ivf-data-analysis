import pandas as pd

df = pd.read_excel(r'C:/Users/MicroApt/Desktop/3600DigiTMG_Project/Data/DataSet.xlsx')
df.info()
df.shape
df.columns

# First Moment Business Decision
#Mean
df.age.mean()
#median
df.age.median()
#mode
df.age.mode()

df['Spouse AGE'].mean()
df['Spouse AGE'].median()
df['Spouse AGE'].mode()

# we only got mode becuse str N
#df['Clinical pregnancy: 0:0, Chemical: 1:1 Positive'].mean()
#df['Clinical pregnancy: 0:0, Chemical: 1:1 Positive'].median()
#df['Clinical pregnancy: 0:0, Chemical: 1:1 Positive'].mode()

df['Live Birth'].mean()
df['Live Birth'].median()
df['Live Birth'].mode()

df['WEEK OF BIRTH'].mean()
df['WEEK OF BIRTH'].median()
df['WEEK OF BIRTH'].mode()

df['Neonatal Death'].dtype
df['Neonatal Death'].mean()
df['Neonatal Death'].median()
df['Neonatal Death'].mode()

df['ABORTION'].dtype
df['ABORTION'].mean()
df['ABORTION'].median()
df['ABORTION'].mode()

df['BHCG 12'].mean()
df['BHCG 12'].median()
df['BHCG 12'].mode()

df['BHCG 14'].mean()
df['BHCG 14'].median()
df['BHCG 14'].mode()

df['BHCG 12-14% increase'].mean()
df['BHCG 12-14% increase'].median()
df['BHCG 12-14% increase'].mode()

df['twin'].mean()
df['twin'].median()
df['twin'].mode()

#Even though numeric. it represents lable, not quantities
#df['Indication Hormonal = 1                                                         \nIndication Unexplained = 2\nIndication Male = 3\nIndication Other/Low = 4\nIndication DOR = 5\nIndication Tubal = 6'].mean()
#df['Indication Hormonal = 1                                                         \nIndication Unexplained = 2\nIndication Male = 3\nIndication Other/Low = 4\nIndication DOR = 5\nIndication Tubal = 6'].median()
#df['Indication Hormonal = 1                                                         \nIndication Unexplained = 2\nIndication Male = 3\nIndication Other/Low = 4\nIndication DOR = 5\nIndication Tubal = 6'].mode()

df['FSH'].mean()
df['FSH'].median()
df['FSH'].mode()

pd.to_numeric(df['PROGESTERONE'], errors='coerce').mean()
pd.to_numeric(df['PROGESTERONE'], errors='coerce').median()
pd.to_numeric(df['PROGESTERONE'], errors='coerce').mode()


df['NUMBER OF OOCYTES'].mean()
df['NUMBER OF OOCYTES'].median()
df['NUMBER OF OOCYTES'].mode()

df['Embryo Tranfer Day'].mean()
df['Embryo Tranfer Day'].median()
df['Embryo Tranfer Day'].mode()

pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').mean()
pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').median()
pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').mode()


df['IND. NUMBER OF DAYS'].mean()
df['IND. NUMBER OF DAYS'].median()
df['IND. NUMBER OF DAYS'].mode()

df['Number of Embryos Transferred'].mean()
df['Number of Embryos Transferred'].median()
df['Number of Embryos Transferred'].mode()

df['EU'].mean()
df['EU'].median()
df['EU'].mode()

df['AMH'].mean()
df['AMH'].median()
df['AMH'].mode()


#################################
# Second Moment Business Decision
#Variance
df.age.var()
#Standard Deviation
df.age.std()
#range
range = max(df.age) - min(df.age)
range

df['Spouse AGE'].var()
df['Spouse AGE'].std()
range = max(df['Spouse AGE']) - min(df['Spouse AGE'])
range

df['Live Birth'].var()
df['Live Birth'].std()
range = max(df['Live Birth']) - min(df['Live Birth'])
range

df['WEEK OF BIRTH'].var()
df['WEEK OF BIRTH'].std()
range = max(df['WEEK OF BIRTH']) - min(df['WEEK OF BIRTH'])
range

df['Neonatal Death'].var()
df['Neonatal Death'].std()
range = max(df['Neonatal Death']) - min(df['Neonatal Death'])
range

df['ABORTION'].var()
df['ABORTION'].std()
range = max(df['ABORTION']) - min(df['ABORTION'])
range

df['BHCG 12'].var()
df['BHCG 12'].std()
range = max(df['BHCG 12']) - min(df['BHCG 12'])
range

df['BHCG 14'].var()
df['BHCG 14'].std()
range = max(df['BHCG 14']) - min(df['BHCG 14'])
range

df['BHCG 12-14% increase'].var()
df['BHCG 12-14% increase'].std()
range = max(df['BHCG 12-14% increase']) - min(df['BHCG 12-14% increase'])
range

df['twin'].var()
df['twin'].std()
range = max(df['twin']) - min(df['twin'])
range

df['FSH'].var()
df['FSH'].std()
range = max(df['FSH']) - min(df['FSH'])
range


# we wrote this column an PROGESTERONE_clean because have only one value as <20 taking as str value
pd.to_numeric(df['PROGESTERONE'], errors='coerce').var()
pd.to_numeric(df['PROGESTERONE'], errors='coerce').std()
range = (
    pd.to_numeric(df['PROGESTERONE'], errors='coerce').max()
    - pd.to_numeric(df['PROGESTERONE'], errors='coerce').min()
)
range


df['NUMBER OF OOCYTES'].var()
df['NUMBER OF OOCYTES'].std()
range = max(df['NUMBER OF OOCYTES']) - min(df['NUMBER OF OOCYTES'])
range

df['Embryo Tranfer Day'].var()
df['Embryo Tranfer Day'].std()
range = max(df['Embryo Tranfer Day']) - min(df['Embryo Tranfer Day'])
range

#because we have only one - value as str so
pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').var()
pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').std()
range = (
    pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').max()
    - pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').min()
)
range

df['IND. NUMBER OF DAYS'].var()
df['IND. NUMBER OF DAYS'].std()
range = max(df['IND. NUMBER OF DAYS']) - min(df['IND. NUMBER OF DAYS'])
range

df['Number of Embryos Transferred'].var()
df['Number of Embryos Transferred'].std()
range = max(df['Number of Embryos Transferred']) - min(df['Number of Embryos Transferred'])
range

df['EU'].var()
df['EU'].std()
range = max(df['EU']) - min(df['EU'])
range

df['AMH'].var()
df['AMH'].std()
range = max(df['AMH']) - min(df['AMH'])
range


################################
# Third Moment Business Decision
#Skewness
df.age.skew()

df['Spouse AGE'].skew()

df['Live Birth'].skew()

df['WEEK OF BIRTH'].skew()

df['Neonatal Death'].skew()

df['ABORTION'].skew()

df['BHCG 12'].skew()

df['BHCG 14'].skew()

df['BHCG 12-14% increase'].skew()

df['twin'].skew()

df['FSH'].skew()
 
#did not work so 
#df['PROGESTERONE_clean'].skew()
pd.to_numeric(df['PROGESTERONE'], errors='coerce').skew()

df['NUMBER OF OOCYTES'].skew()

df['Embryo Tranfer Day'].skew()

df['ENDOMETRIAL_THICKNESS_clean'].skew()

df['IND. NUMBER OF DAYS'].skew()

df['Number of Embryos Transferred'].skew()

df['EU'].skew()

df['AMH'].skew()

################################
# Fourth Moment Business Decision
#Kurtosis
df.age.kurt()

df['Spouse AGE'].kurt()

df['Live Birth'].kurt()

df['WEEK OF BIRTH'].kurt()

df['Neonatal Death'].kurt()

df['ABORTION'].kurt()

df['BHCG 12'].kurt()

df['BHCG 14'].kurt()

df['BHCG 12-14% increase'].kurt()

df['twin'].kurt()

df['FSH'].kurt()

#did not work so 
#df['PROGESTERONE_clean'].skew()
pd.to_numeric(df['PROGESTERONE'], errors='coerce').kurt()

df['NUMBER OF OOCYTES'].kurt()

df['Embryo Tranfer Day'].kurt()

pd.to_numeric(df['ENDOMETRIAL THICKNESS ON THE DAY OF TRANSFER'], errors='coerce').kurt()

df['IND. NUMBER OF DAYS'].kurt()

df['Number of Embryos Transferred'].kurt()

df['EU'].kurt()

df['AMH'].kurt()
