import pandas as pd

def percent_enr(col_name):
    return (round(data[col_name].sum()/all_enrollment*100, 2))

if __name__=="__main__":
    data = pd.read_csv("data/CRDC2013_14.csv")
    data["total_enrollment"] = data["TOT_ENR_F"] + data["TOT_ENR_M"]
    all_enrollment = data["total_enrollment"].sum()
    print("Percent of hispanic male students= ", percent_enr("SCH_ENR_HI_M"))
    print("Percent of hispanic female students= ", percent_enr("SCH_ENR_HI_F"))
    print("Percent of american indian male students= ", percent_enr("SCH_ENR_AM_M"))
    print("Percent of american indian female students= ", percent_enr("SCH_ENR_AM_F"))
    print("Percent of asian male students= ", percent_enr("SCH_ENR_AS_M"))
    print("Percent of asian female students= ", percent_enr("SCH_ENR_AS_F"))
    print("Percent of hawaiian or pacific islander male students= ", percent_enr("SCH_ENR_HP_M"))
    print("Percent of hawaiian or pacific islander female students= ", percent_enr("SCH_ENR_HP_F"))
    print("Percent of black male students= ", percent_enr("SCH_ENR_BL_M"))
    print("Percent of black female students= ", percent_enr("SCH_ENR_BL_F"))
    print("Percent of white male students= ", percent_enr("SCH_ENR_WH_M"))
    print("Percent of white female students= ", percent_enr("SCH_ENR_WH_F"))
    print("Percent of two or more races and male students= ", percent_enr("SCH_ENR_TR_M"))
    print("Percent of two or more races and female students= ", percent_enr("SCH_ENR_TR_F"))

