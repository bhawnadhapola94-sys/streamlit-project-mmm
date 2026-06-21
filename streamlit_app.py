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
    st.subheader("Provider Types Distribution")
    fig, ax = plt.subplots(figsize=(5,3))
    provider['Type'].value_counts().plot(
        kind='line',
        marker='o',
        ax=ax
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Receiver Types Distribution")
    fig, ax = plt.subplots(figsize=(5,3))
    receivers['Type'].value_counts().plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 10 Locations")
    top_locations = (
        food.groupby('Location')['Food_Name']
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(5,3))
    top_locations.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col4:
    st.subheader("Meal Types")
    fig, ax = plt.subplots(figsize=(5,3))
    food['Meal_Type'].value_counts().plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
