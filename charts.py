import altair as alt
import pandas as pd

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
        