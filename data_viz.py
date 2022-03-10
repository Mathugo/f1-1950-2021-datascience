from pickle import NONE
import streamlit as st
import pandas as pd
from load import ETL
from charts import Charts
import matplotlib.pyplot as plt
from pyvis.network import Network
import streamlit.components.v1 as components
from queries import Queries


st.set_page_config(layout="wide")

"""
Run the script : python3 -m streamlit run data_viz.py
"""

conn = ETL.connect()
q = Queries(conn)

st.title("Welcome to f1 data analysis of all seasons !")
st.write("""
# 
""")
st.header("Some interesting facts about f1")
st.subheader('Drivers with the most wins of all time')

data = q.most_win()
st.write(Charts.NumberOfWins(data))

exp = st.expander("Whouawh !", expanded=True)
col1, col2 = exp.columns(2)

with col1:
    st.subheader("Dominant racing team in f1 history ")
    #number of total wins of one ecurie
    df = q.dominant_racing_team()
    st.markdown("Without a doubt, the winnner is still ferrari ")
    st.write(Charts.RacingTeamPie(df))

with col2: 
    st.subheader("Top 5 Drivers with the most pole position")
    df = q.most_pole()
    st.markdown("Again, Sir Lewis Hamilton ..")
    st.write(Charts.MostPolePie(df))
    
st.header("From a BI point of view, what can we get from thoses data ? ")
st.subheader("How often a particular driver out-qualifies his team-mate ?")

data = q.number_of_point()
st.subheader("Evolution of the number of points in the 2021 season")
st.write(Charts.NumberOfPoint(data))
st.markdown("We can see that, although the final winner of the season was not obvious, it apear that Red bull got some big momentum and Mercedes stayed continuously a big challenger for the title.")

st.subheader("Does doing the best lap of the race necessarily win the race?")
data = q.fastest_lap_win()
data['position'] = data['position'].replace(['\\N'],'22')
st.markdown("By summing the position of the drivers with the fastest lap, we can see that it is not correlated to the fastestLap")
st.write("Average position when driver have the fastestLap : "+str(round(Charts.Fastestlap(data), 2)))

st.subheader("By doing very short pitstops, does it influence the team overall performance ?")
st.markdown("Let's print out the shortest pitstop with the position of the driver ! ")

data = q.pitstop_position()
st.write(Charts.PitStop(data))



"""
st.subheader("Network")
HtmlFile = open("nx.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 900,width=900)

st.write(Charts.Network())
"""


st.markdown("""
 evolution du numbre de point au championship dans le top 5 en 2021 (saison intéressante)
 faire correler ce résultat avec .. 

 driver with the most number of wins at a particular track 

pits stop -> est ce que ça a un impacte sur le classement ? 
""")

st.markdown(""" correlation entre fastest lap et win ? """)
