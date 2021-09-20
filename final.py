import pandas as pd
import csv
import plotly_express as px
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
student_df=df.loc[df['student_id']=="TRL_987"]
print(student_df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=['level 1','level 2','level 3','level 4'],
    y=student_df.groupby("level")["attempt"].mean(),
    orientation='v'
))
fig.show()
