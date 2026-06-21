import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Food Wastage Dashboard", layout="wide")

# Load CSV files
provider = pd.read_csv("providers.csv")
receivers = pd.read_csv("receivers.csv")
claims = pd.read_csv("claims.csv")
food = pd.read_csv("food_list.csv")

st.title("Food Wastage Management Dashboard")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Providers", len(provider))
col2.metric("Receivers", len(receivers))
col3.metric("Food Items", len(food))
col4.metric("Claims", len(claims))
st.markdown("---")
st.header("Overview")

col1, col2 = st.columns(2)

with col1:
   provider_count = provider['Type'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(5,3))
provider_count.plot(
    kind='line',
    marker='o',
    linewidth=2,
    ax=ax
)

ax.set_xlabel("Provider Type")
ax.set_ylabel("Count")
ax.set_title("Provider Type Distribution")
plt.xticks(rotation=45)

st.pyplot(fig)
with col2:
    st.subheader("Receiver Types Distribution")
    fig, ax = plt.subplots()
    receivers['Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    location_count = (
    food.groupby('Location')['Food_Name']
    .count()
    .sort_values(ascending=False)
    .head(10)
)

location_count.plot(kind='barh', ax=ax)
ax.set_xlabel("Food Count")
ax.set_ylabel("Location")
ax.set_title("Top 10 Locations by Food Count")

with col2:
    st.subheader("Meal Types")
    fig, ax = plt.subplots()
    food['Meal_Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

st.markdown("""
This dashboard provides insights into food donations,
providers, receivers, and claims to help reduce food wastage.
""")
