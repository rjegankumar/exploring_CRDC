import pandas as pd

if __name__=="__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    print(data["JJ"].value_counts())
    print(data["SCH_STATUS_MAGNET"].value_counts())
    print("Male and Female counts in Juvinile Justice and non-Juvinile Justice Facilities")
    print(pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index="JJ", aggfunc="sum"))
    print("Male and Female counts in Magnet schools and non-Magent schools")
    print(pd.pivot_table(data, values=["TOT_ENR_M","TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum"))
