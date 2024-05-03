import streamlit as st


st.title("Questions")

st.subheader("Q1- What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.")

st.write("""The project was initially set up to explore relationships between urbanization (as indicated by population) and environmental factors such as water temperature and pollution levels in cities. This study aimed to determine if more populated areas experienced higher pollution and temperature changes, potentially impacting local climates and health standards.
""")

st.subheader("Q2- What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?")

st.write("After analyzing the data, cities with larger populations did not necessarily have higher levels of water pollution and water temperatures. The results could suggest that industrial and residential waste do not contribute significantly to pollution and that temperature changes are also influenced by a broader set of regional and environmental factors.")

st.subheader("Q3- What difficulties did you have in completing the project?")

st.write("Some challenges include dealing with incomplete or noisy data, integrating data from various sources, and developing a reliable method for real-time data analysis and visualization. Overall, there were also technical issues with software or coding errors because I realized that I had to make sure that all the coding texts matched the dataset texts. I also had to convert the formatting of my csv data into sole values because if the water temperature had the Farenheit of celsius sign, it would not be read by code. 
")

st.subheader("Q4- What skills did you wish you had while you were doing the project?")

st.write("During the project, I wish I had the stronger skill in making my web app more dynamic and interactive. For example, I wish I was able to add a mapping visualization of the cities rather than just having some bar graphs. 
")

st.subheader("Q5- What would you do “next” to expand or augment the project?")

st.write("
To expand the project, I was considering incorporating additional environmental factors such as air quality and land use data. Another direction could be to apply machine learning models to predict future pollution levels and temperatures based on current trends and urban development policies.
")

