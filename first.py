import pandas as pd
data={
    "apples":[4,3,5,6],
    "oranges":[1,3,2,6]
}
index=['aron','lee','steve','harry']
purchases=pd.DataFrame(
    data,index=index
)

# purchases=pd.DataFrame(data)
print(purchases)
# print(purchases.dtypes)

# print(purchases["apples"])
print(purchases.loc["aron"])

