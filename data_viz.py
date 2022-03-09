import streamlit as st
import pandas as pd
from load import ETL
from charts import Charts
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

"""
Run the script : python3 -m streamlit run data_viz.py
"""

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

    def number_of_point(self, year=2021):
        """ number of point per team during a year"""
        query = """
        select r."resultId", r."raceId", points, r."constructorId", c."name", rc."year", rc.date from results r
        inner join races rc ON r."raceId" = rc."raceId"
        inner join constructors c ON r."constructorId" = c."constructorId"
        where year=2021
        order by c."constructorId"
        """
        df = pd.read_sql_query(query, self.conn)
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
    
data = q.number_of_point()
st.write(data)

st.write(Charts.NumberOfPoint(data))

st.markdown("""
 evolution du numbre de point au championship dans le top 5 en 2021 (saison intéressante)
 faire correler ce résultat avec .. 

 driver with the most number of wins at a particular track 

pits stop -> est ce que ça a un impacte sur le classement ? 
""")

st.markdown(""" correlation entre fastest lap et win ? """)

st.header("From a BI point of view, what can we get ? ")
st.subheader("How often a particular driver out-qualifies his team-mate ?")