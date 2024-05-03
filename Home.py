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

import streamlit as st
from streamlit.logger import get_logger

st.title("DSCI 510 Final")
st.title(" 'Water pollution and water temperature analysis based on city and population' ")

st.subheader("by Elisa Xia")

st.subheader("An explanation of how to use your webapp: what interactivity there is, what the plots/charts mean, what your conclusions were, etc.")

st.write("The webapp allows users to interactively explore a dataset containing information about cities, temperatures, populations, and water pollution levels. On the left sidebar, users can select one or more regions of interest from a multiselect dropdown menu. There is also a slider that lets users set a threshold for water pollution levels. For the water temperatures, you can also choose from the dropdown of minimum, maximum or average water temperature. 
The first three visualizations show bar graphs of variables depicted by cities. Then, the following three visualizations show scatter plots and correlations between variables. 
For example, there is a bar graph showing the relationship between population size (x-axis) and water pollution levels (y-axis), with water pollution threshold, which allows users to identify potential correlations or outliers. There is also a visualization of the average water temperature for each selected region, giving insights into climatic variations. 
Overall, the results from my data show that there is not much correlation between water temperature, water pollution and population. In fact, I observed that some cities that have the same population have various different water temperatures. This makes sense because cities like Los angeles and New York City might have the same population, but since they are on two different sides of the coast, their water temperatures are very different. I expected there to be a positive correlation because the higher the population, the more urbanization. I guessed that this urbanization would’ve increased the water temperatures. Additionally, higher energy consumption in denser populations leads to increased discharge of warm water from industrial processes, further raising water body temperatures. However, this visualization shows that population is not the only factor affecting water temperatures since there are geographical factors which affect tenperature more. Similarly, for water pollution, just because a city had higher population, it did not translate to a higher pollution because there could be potentially better regulations on water cleanings in higher density/more urban cities. 
By utilizing these interactive filters and visualizations, users can draw conclusions about factors like which regions have higher populations and pollution levels, if there are associations between population density and environmental quality, how temperatures vary geographically, and more. The dynamic nature of the plots enables exploring the data through multiple lenses to uncover patterns and potential areas of concern or interest. Overall, this webapp facilitates a comprehensive visual analysis of the underlying urban environmental dataset.
")

st.subheader("Any major gotchas, i.e. things that don’t work, go slowly, could be improved, etc.")

st.write("One of the major gotchas from working on this webapp is that I realized that there is not as much correlation between variables as I expected there to be. This may be because the dataset that I used might not have been extensive enough, or instead of testing human population of cities, I could’ve tested a more relevant variable, such as the population of a certain seawater animal. This might have made more sense because my pollution and temperature variables were related to the water setting. ")

