import pandas as pandas
df=pd.read_excel("day14.xls")
df["mark"]=df["mark"]+10
print(df)
df.to_excel(excel_writer:"res.xlsx",index=False)