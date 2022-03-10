import altair as alt
import pandas as pd
from sqlalchemy import false, null
import numpy as np 
from pyvis.network import Network
import networkx as nx
from IPython.core.display import display, HTML

pd.options.mode.chained_assignment = None  # default='warn'


class Charts:

    @staticmethod
    def NumberOfWins(df):
        return alt.Chart(df).mark_bar().encode(
        y='total_wins',
        x='surname',
        color='nationality'
).properties(
    width=1400,
    height=500
)

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
    def Network(df=None):
        nx_graph = nx.cycle_graph(10)
        nx_graph.nodes[1]['title'] = 'Number 1'
        nx_graph.nodes[1]['group'] = 1
        nx_graph.nodes[3]['title'] = 'I belong to a different group!'
        nx_graph.nodes[3]['group'] = 10
        nx_graph.add_node(20, size=20, title='couple', group=2)
        nx_graph.add_node(21, size=15, title='couple', group=2)
        nx_graph.add_edge(20, 21, weight=5)
        nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
        nt = Network('500px', '500px')
        # populates the nodes and edges data structures
        nt.from_nx(nx_graph)
        nt.show('nx.html')
        return display(HTML('nx.html'))

    @staticmethod
    def NumberOfPoint(df):  
        # delete name 
        df_plot = df.query("name != 'Williams' and name != 'Haas F1 Team' and name != 'Alfa Romeo' and name!= 'Aston Martin'")
        # calculate cumulative point 
        df_plot["cumulativepoints"] = 0
        previous_value = 0
        for name in ["Ferrari", "Mercedes", "AlphaTauri", "Red Bull", "McLaren", "Alpine F1 Team"]:            
            for i in range(1, len(df_plot)):
                if df_plot["name"].iloc[i] == name:
                    cum = df_plot["cumulativepoints"]
                    df_plot["cumulativepoints"].iloc[i] = previous_value + df_plot["points"].iloc[i]
                    previous_value = df_plot["cumulativepoints"].iloc[i]
            previous_value = 0
        return alt.Chart(df_plot).mark_line().encode(
            x='date:T',
            y='cumulativepoints:Q',
            color='name:N'
        ).properties(
    width=1400,
    height=500
)
    @staticmethod
    def PitStop(df):
        # mean of pit stop 
        # mean of position 
        print(df)
        means = []
        """
        for name in pd.unique(df["surname"]):
            pos = 0
            duration = 0
            data = df[df["surname"] == name]
            for i in range(0, len(df)):
                pos += float(data["position"].iloc[i])
                duration += float(data["milliseconds"].iloc[i])

            means.append(df.mean(axis=0))
            #print(str(means))
            print(name)
        """

        return alt.Chart(df).mark_point().encode(
        x='mean(duration)',
        y='position',
        color='surname'
)

    @staticmethod
    def Fastestlap(df):
        position = df["position"].astype(int)
        return position.sum(axis=0) / len(df)
        """
        base = alt.Chart(df).encode(
            alt.X('date:T', axis=alt.Axis(title="date of grand prix of 2021"))
        )

        area = base.mark_point(opacity=0.3, color='#57A44C').encode(
            alt.Y('position',
                axis=alt.Axis(title='Position', titleColor='#57A44C')),
            alt.Y2('average(position'),
            alt.Color('surname:N')
        )

        line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
            alt.Y('time',
                axis=alt.Axis(title='FastestLap', titleColor='#5276A7' )),
                alt.Color('surname:N')
        )

        layer = alt.layer(area, line).resolve_scale(
            y = 'independent'
        )
        return layer
        """
        
 