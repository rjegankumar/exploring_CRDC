import pandas as pd

if __name__=="__main__":
    contents = pd.read_csv("data/CRDC2013_14content.csv")
    print("First five rows:")
    print(contents.head(5))
    print("(Rows, Columns):")
    print(contents.shape)
    print("Unique values and their counts in the 'TYPE' column:")
    print(contents['TYPE'].value_counts())
    print("Unique values and their counts in the 'PART' column:")
    print(contents['PART'].value_counts())
    print("Unique values and their counts in the 'QUESTION' column:")
    print(contents['QUESTION'].value_counts())
    pd.set_option('display.max_rows', None)
    print("all values in 'NAME' and 'LABEL':")
    print(contents.loc[:,['NAME','LABEL']])
