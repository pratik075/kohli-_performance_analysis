import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#read the csv file
df=pd.read_csv("dataset.csv")
print(df.head(10))

#find total number of runs kohli has scored
total_runs=df["Runs"].sum
no_of_matches=len(df["Runs"])
print(f"Total no of run kohli has scored  in {no_of_matches} matches",total_runs)

#average of number of runs he has played at different position
avg_runs=df["Runs"].mean()
print(f"average score of kohli in {no_of_matches} matches:",avg_runs)
#no of matches he has played at diffferent position

position=df["Pos"].unique()
print(position)
df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    2.0:"Batting at 2",
    1.0:"Batting at 1",
    7.0:"Batting at 7",
    5.0:"Batting at 5",
    7.0:"Batting at 6"





})
print(df[["Runs","Pos","Opposition"]].head())

def show_pie_plot(df,key):
    counts=df[key].value_counts()
    count_values=counts.values
    count_labels=counts.index

    fig=plt.figure(figsize=(10,7))
    plt.pie(count_values,labels=count_labels)
    plt.show()

show_pie_plot(df,"Pos")
show_pie_plot(df,"Opposition")
show_pie_plot(df,"Ground")
pos_counts=df["Pos"].value_counts()
print(pos_counts)

pos_values=pos_counts.values
pos_labels=pos_counts.index
print(pos_values)


#total runs scores in different position
pos_counts=df["Pos"].value_counts()
print(pos_counts)
pos_values=pos_counts.values
pos_labels=pos_counts.index
print(pos_values)
fig=plt.figure(figsize=(10,7))
plt.pie(pos_values,labels=pos_labels)
plt.show()
#pie chart on opponent
opponent_counts=df["Opposition"].value_counts()
#total runs scores in different position

runs_at_pos=df.groupby("Pos")["Runs"].sum()
print(runs_at_pos)
runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index
fig=plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values,labels=runs_at_pos_labels)
plt.show()

#total sixes with different opposition
sixes_with_ops=df.groupby("Opposition")["6s"].sum()
sixes_with_ops_values=sixes_with_ops.values
sixes_with_ops_labels=sixes_with_ops.index

fig=plt.figure(figsize=(10,7))
plt.pie(sixes_with_ops_values,labels=sixes_with_ops_labels)
plt.show()
print(sixes_with_ops)



#no of centuries score by kohli in first and second inning

centuries=df.query("Runs>=100")
print(centuries)

innings=centuries["Inns"]
tons=centuries["Runs"]

# print(innings)
fig=plt.figure(figsize=(10,7))
plt.bar(innings,tons,color='blue',width=0.2)
plt.show()

#calculate of dismissal of kohli

dismissals=df["Dismissal"].value_counts()
print(dismissals)

dismissals_counts=dismissals.values
dismissals_labels=dismissals.index
show_pie_plot(df,"Dismissal")
#against which team he has scored  most run

fig=plt.figure(figsize=(10,7))
plt.bar(
    df["Opposition"],df["Runs"],color='red',width=0.1
)
plt.show()
#against which team he has scored most centuries
#kohli's struke in first inning vs second inning
#run scored by kohli 