import altair as alt
import pandas as pd
from sqlalchemy import null
import matplotlib
import numpy as np 

class Charts:

    @staticmethod
    def RacingTeamPie(df):
        source = pd.DataFrame(
            {"category": df["name"], "value": df["total_wins"]}
        )
        alt.Chart(source).mark_arc().encode
        base = alt.Chart(source).encode(
            theta=alt.Theta("value:Q", stack=True), color="value:N",
        )   
        pie = base.mark_arc(outerRadius=110)
        text = base.mark_text(radius=130, size=12).encode(text="category:N")
        return pie + text
    
    @staticmethod
    def MostPolePie(df):
        source = pd.DataFrame(
            {"category": df["surname"], "value": df["total_pole"]}
        )
        base = alt.Chart(source).encode(
            theta=alt.Theta("value:Q", stack=True),
            radius=alt.Radius("value", scale=alt.Scale(type="sqrt", zero=True, rangeMin=20, rangeMax=130)),
            color="value:N",
        )
        c1 = base.mark_arc(innerRadius=20, stroke="#fff")
        text = base.mark_text(radiusOffset=30, size=10).encode(text="category:N")
        return c1 + text

    @staticmethod
    def NumberOfPoint(df):  
        # delete name 
        df_plot = df.query("name != 'Williams' and name != 'Haas F1 Team' and name != 'Alfa Romeo' and name!= 'Aston Martin'")
        
        # calculate cumulative point 

        df_plot["cumulativepoints"] = 0
        previous_value = 0
        for name in ["Ferrari", "Mercedes", "AlphaTauri", "RedBull", "McLaren", "Alpine F1 Team"]:            
            for i in range(1, len(df_plot)):
                if df_plot["name"].iloc[i] == name:
                    df_plot["cumulativepoints"].iloc[i] = previous_value + df_plot["points"].iloc[i]
                    previous_value = df_plot["cumulativepoints"].iloc[i]
                    print("Name : "+df_plot["name"].iloc[i]+"Points : "+str(df_plot["cumulativepoints"].iloc[i]))
            previous_value = 0

        print(df_plot)
        df_plot
        return alt.Chart(df_plot).mark_line().encode(
            x='date:T',
            y='cumulativepoints:Q',
            color='name:N'
        ).properties(
    width=1400,
    height=500
)
        
    

        """alt.X('monthdate(date):O', title='Grand Prix f1'),
            alt.Y('Q(points):O', title='Points'),
            alt.Color('name:Q', title="Team")"""
"""
return alt.Chart(df_plot).mark_trail().encode(
            x='date:T',
            y='points:Q',
            color='name:N'
        ).properties(
    width=1400,
    height=500
).transform_aggregate(
    points='sum(points)',
    groupby=["name", "date"],
)
"""