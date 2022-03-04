from typing import Any
import streamlit as st
import pandas as pd
from load import ETL
import sqlalchemy as sa
import sys 
import numpy as np
from charts import Charts

st.set_page_config(layout="wide")

"""
Run the script : python3 -m streamlit run data_viz.py
"""

# 2eme couche dimension et fait 
# table finale data mart


class Queries:
    def __init__(self, conn) -> None:
        self.conn = conn
    
    def most_win(self) -> list: 
        """ get the driver with the most win"""
        query = """select * from (
        select count(position) as total_wins, ds."driverId" 
        from driver_standings ds where position = 1 
        group by ds."driverId" 
        order by total_wins desc
        limit 5) as ds
        inner join drivers d ON ds."driverId" = d."driverId"
        """
        df = pd.read_sql_query(query, self.conn)
        del df["driverId"]
        del df["number"]
        return df
    
    def dominant_racing_team(self) -> list:
        """ get the most dominant team in f1"""
        query = """
        select * from (
        select count(wins) as total_wins, cr."constructorId" 
        from constructor_standings cr
        group by cr."constructorId" 
        order by total_wins desc
        limit 5) as cr
        inner join constructors c ON c."constructorId" = cr."constructorId"
        """
        df =  pd.read_sql_query(query, self.conn)
        del df["constructorId"]
        del df["constructorRef"]
        return df
    
    def most_pole(self) -> list:
        """ get the driver with the most pole """
        query = """
        select * from (
        select count(position) as total_pole, ql."driverId" 
        from qualifying ql where position = 1
        group by ql."driverId" 
        order by total_pole desc
        limit 5) as ql
        inner join drivers d ON d."driverId" = ql."driverId"
        """
        df = pd.read_sql_query(query, self.conn)
        del df["driverId"]
        del df["number"]
        del df["forename"]
        return df


conn = ETL.connect()
q = Queries(conn)

st.title("Welcome to f1 data analysis of all seasons !")
st.write("""
# 
""")
st.header("Some interesting facts about f1")
st.subheader('Drivers with the most wins of all time')

data = q.most_win()
st.write(data)

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
    


st.markdown("""
 evolution du numbre de point au championship dans le top 5 en 2021 (saison intéressante)
 faire correler ce résultat avec .. 

 driver with the most number of wins at a particular track 

""")

st.header("From a BI point of view, what can we get ? ")
st.subheader("How often a particular driver out-qualifies his team-mate ?")