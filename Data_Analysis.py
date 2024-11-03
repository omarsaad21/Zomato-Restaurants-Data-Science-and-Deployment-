import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt  # Ensure this import is included
import seaborn as sns  # Ensure seaborn is imported



# Title of the Analysis page
st.title("Zomato Project Analysis")

st.write("""
## Overview of Restaurant Data Analysis

This analysis provides key insights into various aspects of restaurant data, focusing on customer engagement and cost distributions across different categories. The visualizations below highlight important trends, such as the popularity of online ordering, table booking patterns, and geographic concentration of restaurant activity.

Key metrics such as average votes per location and the average cost for two people grouped by restaurant type ('listed_in(type)') offer a deeper understanding of customer preferences and spending habits. These insights can guide decision-making around service offerings and location-based strategies.

Each chart provides a breakdown of significant features within the dataset, enabling us to observe patterns, identify outliers, and draw conclusions about the overall performance and preferences of restaurants in different areas.

""")


# Read the CSV file directly (replace 'your_file.csv' with the actual file name)
df = pd.read_csv("D:\Epsilon AI internship\Project_1\cleaned_data.csv")  # Make sure this is a CSV file



# Set up the Streamlit app title
st.title('Restaurant Data Visualizations')

# Display the first chart: Online Order Distribution
st.subheader('Online Order Distribution')
fig1, ax1 = plt.subplots()
sns.countplot(data=df, x='online_order', ax=ax1)
ax1.set_title('Online Order Distribution')
st.pyplot(fig1)  # Render the plot in Streamlit

# Display the second chart: Book Table Distribution
st.subheader('Book Table Distribution')
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='book_table', ax=ax2)
ax2.set_title('Book Table Distribution')
st.pyplot(fig2)

# Bar plot for top 10 most frequent locations
st.subheader('Top 10 Locations')
top_locations = df['location'].value_counts().head(10)
fig3, ax3 = plt.subplots()
sns.barplot(x=top_locations.index, y=top_locations.values, ax=ax3)
ax3.set_title('Top 10 Locations')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)  # Rotate x labels
st.pyplot(fig3)

# Bar plot for top 10 most frequent cuisines
st.subheader('Top 10 Cuisines')
top_cuisines = df['cuisines'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=top_cuisines.index, y=top_cuisines.values, ax=ax4)
ax4.set_title('Top 10 Cuisines')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)  # Rotate x labels
st.pyplot(fig4)

# Set up the Streamlit app title
st.title('Numeric Columns Histograms')

# Plot histograms for numeric columns
st.subheader('Votes and Approx Cost Histograms')

# Create the histogram for the numeric columns
fig, ax = plt.subplots(figsize=(10, 6))
df[['votes', 'approx_cost(for two people)']].hist(bins=20, ax=ax)
plt.tight_layout()

# Display the histogram in Streamlit
st.pyplot(fig)


# Set up the Streamlit app title
st.title('Correlation Matrix for Numeric Columns')

# Correlation matrix for numeric columns
st.subheader('Votes and Approx Cost Correlation Matrix')
corr_matrix = df[['votes', 'approx_cost(for two people)']].corr()

# Create the heatmap for the correlation matrix
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)

# Display the heatmap in Streamlit
st.pyplot(fig)


# Set up the Streamlit app title
st.title('Average Votes per Location')

# Compute the average votes per location and take the top 10
location_votes = df.groupby('location')['votes'].mean().sort_values(ascending=False).head(10)

# Create the bar plot
st.subheader('Top 10 Locations by Average Votes')
fig, ax = plt.subplots(figsize=(10, 6))
location_votes.plot(kind='bar', ax=ax)
ax.set_title('Average Votes per Location')
ax.set_ylabel('Average Votes')

# Display the bar plot in Streamlit
st.pyplot(fig)

# Set up the Streamlit app title
st.title('Average Approx Cost by Listing Type')

# Compute the average cost by listed_in(type)
st.subheader('Average Approx Cost by Listing Type')
avg_cost_by_type = df.groupby('listed_in(type)')['approx_cost(for two people)'].mean().sort_values()

# Create the horizontal bar plot
fig, ax = plt.subplots(figsize=(10, 6))
avg_cost_by_type.plot(kind='barh', ax=ax)
ax.set_title('Average Approx Cost by Listing Type')
ax.set_xlabel('Average Approx Cost (for two people)')

# Display the plot in Streamlit
st.pyplot(fig)