"""
Class: CS230--Section 4 
Name: Diego Lopez Sepulveda
Description: (Final Project)
I pledge that I have completed the programming assignment independently. 
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt


DATA_URL = ('Skyscrapers_2021.csv')
data = pd.read_csv("Skyscrapers_2021.csv")

st.title('Famous Skyscrapers')

st.subheader('Oldest Skyscrapers')
st.write("Some of the tallest skyscrapers were not even made in the 21st century!")
oldest = data.loc[data["COMPLETION"] < 2000]
OldestNames = oldest.iloc[:, [1, 2, 6]]
OldestNames = OldestNames.sort_values(by=data.columns[6], ascending=True)

newest = data.loc[data["COMPLETION"] > 2000]
NewestNames = newest.iloc[:, [1, 2, 6]]
NewestNames = NewestNames.sort_values(by=data.columns[6], ascending=False)


SB = st.selectbox('Select to see:', ["Before 2000", "After 2000", "All Ascending", "All Descending"])
if SB == "Before 2000":
    st.write(OldestNames)
elif SB == "After 2000":
    st.write(NewestNames)
elif SB == "All Ascending":
    st.write(data.sort_values(by=data.columns[6], ascending=True).iloc[:, [1, 2, 6]])
    st.image('ESB.png')
elif SB == "All Descending":
    st.write(data.sort_values(by=data.columns[6], ascending=False).iloc[:, [1, 2, 6]])
    st.image('SLS.png')
    st.image('EBS.jpeg')

st.subheader('Building Blocks')
file = data.loc[data[data.columns[11]].isin(['steel', 'steel/concrete', 'concrete', 'composite'])]
column = file[data.columns[11]]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in column:
    if i == 'steel':
        count1 += 1
    elif i == 'steel/concrete':
        count2 += 1
    elif i == 'concrete':
        count3 += 1
    elif i == 'composite':
        count4 += 1

TotalCounts = [count1, count2, count3, count4]
fig, ax = plt.subplots()
ax.bar(range(4),TotalCounts,color='black')
ax.set_xlabel('Materials')
ax.set_title('What is The Main Material?')
ax.set_xticks(range(4))
ax.set_xticklabels(['Steel', 'Steel/Concrete', 'Concrete', 'Composite'])
st.pyplot(fig)


latitude = data[data.columns[4]]
longitude = data[data.columns[5]]
name = data[data.columns[1]]
df = pd.DataFrame({"latitude": latitude, "longitude": longitude, "name": name})
st.subheader('Map of All the Skyscrapers')
st.map(df)


st.subheader(f'Are you Younger than a Skyscraper?')
slide = st.slider("Put your age")
OldCol = file[data.columns[6]]
OldCount = 0
for i in OldCol:
    if (2022-slide) < i:
        OldCount += 1
st.write(f'You are older than {OldCount} Skyscrapers out of 100!')
