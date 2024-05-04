# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def load_data(filepath):
    # Load the dataset from a CSV file
    return pd.read_csv(filepath)

# Load the data
df = load_data('city_temp_population_pollution_data.csv')
df = df[df["Population"]!="Population data not available"]
df["Population"] =  pd.to_numeric(df["Population"])
def filter(string):
    string = string.replace('"','')
    return string

st.title("Visualization and charts")
df['Region'] = df['Region'].apply(filter)

list_regions = list(df['Region'].unique())

st.sidebar.header("Select Region")
selected_Region = st.multiselect("Choose region",df['Region'].unique(),default=list_regions[:5])
df_region = df[df["Region"].isin(list(selected_Region))]

st.subheader("Population of cities in different regions")
  # Create a scatter plot
fig = px.bar(df_region,x='city', y='Population',title="Population of Cities")
# Improve readability of the x-axis labels
fig.update_layout(
    xaxis_tickangle=-45,  # Rotate labels for better readability
    xaxis_title="City",
    yaxis_title="Population",
    hovermode="closest"  # Show tooltip for the closest point
)

# Adjust the marker size to reflect the population size (optional)
fig.update_traces(marker=dict(size=8, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

    # Display the plot in Streamlit
st.plotly_chart(fig)
st.write("Fig. explanation: This bar chart shows population of cities, filterable by Region/State")

st.subheader("Average Water Temperature of Cities in different regions")
fig = px.bar(df_region,x='city', y='average water temperature F',title="Temperature of Water in Cities")
fig.update_layout(
    xaxis_tickangle=-45,  # Rotate labels for better readability
    xaxis_title="City",
    yaxis_title="Water Temperature",
    hovermode="closest"  # Show tooltip for the closest point
)

# Adjust the marker size to reflect the population size (optional)
fig.update_traces(marker=dict(size=8, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))

    # Display the plot in Streamlit
st.plotly_chart(fig)
st.write("Fig. explanation: This bar chart shows water temperatures of cities, filterable by Region/State")

def plot_city_water_pollution(data, pollution_threshold):
    # Filter data based on the pollution threshold
    filtered_data = data[data['WaterPollution'] < pollution_threshold]
    filtered_data = filtered_data.sort_values(by='WaterPollution', ascending=False)
    
    fig = px.bar(filtered_data,x='city', y='WaterPollution',title="Water Pollution in Cities")
    fig.update_layout(
    xaxis_tickangle=-45,  # Rotate labels for better readability
    xaxis_title="City",
    yaxis_title="Water Pollution",
    hovermode="closest"  # Show tooltip for the closest point'
    )
    # Adjust the marker size to reflect the population size (optional)
    fig.update_traces(marker=dict(size=8, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
    return fig


st.title("City Water Pollution Data Visualization")

# Load data
data = load_data('city_temp_population_pollution_data.csv')

# Interactive slider to select the pollution threshold
pollution_threshold = st.sidebar.slider("Select Water Pollution Threshold", 
                                        float(data['WaterPollution'].min()), 
                                        float(data['WaterPollution'].max()), 
                                        step=0.1,value=40.0)

st.write(f"Visualizing Cities with Water Pollution Index Below {pollution_threshold}")
fig = plot_city_water_pollution(data, pollution_threshold)
st.plotly_chart(fig)
st.write("Fig. explanation: This bar chart shows the level of water pollution of cities, interactive by water pollution threshold")

st.sidebar.header("Select min,max, avg temp")
temp_range = ["Min Temp","Max Temp","Avg Temp"]
select_temp = st.sidebar.selectbox("choose",temp_range)

dict1 = {
    "Min Temp" :"min water temperature F",
    "Max Temp": "max water temperature F",
    "Avg Temp": "average water temperature F"
}


st.subheader("Correlation between Population and Water Pollution")
corr = df['WaterPollution'].corr(df['Population'])
st.write(f"correlation coefficient between Population and Pollution : {corr}")
plt.figure(figsize=(12, 8))
sns.regplot(df,x='Population',y='WaterPollution')
plt.xlabel('WaterPollution')
plt.ylabel(dict1[select_temp])
plt.title(f'Correlation of Population and Pollution')
plt.xticks(rotation=80)  # Rotates city names to avoid overlap
plt.tight_layout()  # Adjusts subplots to give some padding
st.pyplot(plt)
st.write("Fig. explanation: This scatterplot graph shows the correlation between population and water pollution, along with its correlation coefficient")


st.subheader("Correlation between Population and Water Temperature")
corr = df['Population'].corr(df[dict1[select_temp]])
st.write(f"correlation coefficient between {dict1[select_temp]} and population : {corr}")
plt.figure(figsize=(12, 8))
sns.regplot(df,x='Population',y=dict1[select_temp])
plt.xlabel('Population')
plt.ylabel(dict1[select_temp])
plt.title(f'Correlation of {dict1[select_temp]} and population')
plt.xticks(rotation=80)  # Rotates city names to avoid overlap
plt.tight_layout()  # Adjusts subplots to give some padding
st.pyplot(plt)
st.write("Fig. explanation: This scatterplot graph shows the correlation between population and water temperature, along with its correlation coefficient")

st.subheader("Correlation between Water Pollution and Water Temperature")
corr = df['WaterPollution'].corr(df[dict1[select_temp]])
st.write(f"correlation coefficient between {dict1[select_temp]} and Pollution : {corr}")
plt.figure(figsize=(12, 8))
sns.regplot(df,x='WaterPollution',y=dict1[select_temp])
plt.xlabel('WaterPollution')
plt.ylabel(dict1[select_temp])
plt.title(f'Correlation of {dict1[select_temp]} and Pollution')
plt.xticks(rotation=80)  # Rotates city names to avoid overlap
plt.tight_layout()  # Adjusts subplots to give some padding
st.pyplot(plt)
st.write("Fig. explanation: This scatterplot graph shows the correlation between water pollution and water temperature, along with its correlation coefficient")

