import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("student.csv")
#Student_ID,Study_Hours,Attendance_Percentage,Parental_Education,Internet_Access,Sleep_Hours,Previous_Grade,Final_Score
# print(df.head())
avg_study_hour=df['Study_Hours'].mean()
avg_final_score=df['Final_Score'].mean()
max_final_score=df['Final_Score'].max()
min_final_score=df['Final_Score'].min()
prev_max_final_score=df['Final_Score'].max()
prev_min_final_score=df['Final_Score'].min()
#student marks to studytime
# plt.figure(figsize=(8,6))
# print(df.head())
# sns.set_context("talk")

# sns.set_style("whitegrid")
# sns.regplot(data=df,x="Study_Hours",y="Final_Score",) 

# plt.axhline(avg_final_score,color="red",linestyle="--")
# sns.despine()
# plt.yticks(range(min_final_score, 100, 5))

# plt.xlabel("Study Hours per Day")
# plt.ylabel("Final Score")
# plt.title("Study Time vs Final score")


# plt.show()

#  #boxplot for student marks to studytime
# plt.figure(figsize=(8,6))
# sns.boxplot(data=df, x="Study_Hours", y="Final_Score")
# plt.title("Distribution of Final Scores by Study Hours")
# plt.show()


# attendance vs performance

# plt.figure(figsize=(8,6))
# sns.set_style("whitegrid")
# sns.scatterplot( data=df,x="Attendance_Percentage", y="Final_Score",)
# plt.yticks(range(35, 101, 5))
# sns.regplot(
#     data=df,
#     x="Attendance_Percentage",
#     y="Final_Score",
#     scatter=False,
#     color="red"
# )
# sns.despine()
# plt.ylabel("MarksObtain")
# plt.xlabel("Attendance")
# plt.title("Attendance (%) vs Final Score Density")
# plt.savefig(
#     "plots/attendance_vs_performance.png",
#     dpi=300,
#     bbox_inches="tight"
# )
# plt.show()


plt.show()