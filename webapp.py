import pandas as pd
import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute("SELECT Date FROM Climate")
date = cursor.fetchall()
date = [item[0] for item in date]
print(date)

cursor.execute("SELECT Temperature FROM Climate")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]
print(temperature)

figure = px.line(x=date, y=temperature, labels={"x:": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
