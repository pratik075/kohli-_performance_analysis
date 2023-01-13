import pandas as pd
df=pd.read_csv("dataset.csv")

# print(df)
# print(df.head(10))
# print(df.tail(10))
print(df.info())
print(df.shape)
# print(df.describe())
print(df["Opposition"].describe())

print(df["Runs"].value_counts())



new_df=df[["Runs","4s","6s","Opposition"]] #extracting desirable data
print(new_df)

print(new_df.iloc[2])  #extracting row
print(new_df.iloc[2:5])
print(new_df.iloc[2]["Runs"])#extracting  score in row 2
print(new_df.iloc[2:5]["Runs"])

vs_aussies =df[df["Opposition"]=="v Australia"]
print(vs_aussies.head(10))
# centuries=vs_aussies[vs_aussies["Runs"]>=100]
# print(centuries)

centuries=df[(df["Opposition"]=="v Australia")& (df["Runs"]>=100)]
# print(centuries)


def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"]=df["Runs"].apply(find_centuries)
print(df)



# print(vs_aussies["Runs"].sum())

