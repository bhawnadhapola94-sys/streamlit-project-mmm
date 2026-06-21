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
    fig, ax = plt.subplots()
    provider['Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Receiver Types Distribution")
    fig, ax = plt.subplots()
    receivers['Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
    col1, col2 = st.columns(2)

with col1:
    st.subheader("Food Count by Location")
    fig, ax = plt.subplots()
    food.groupby('Location')['Food_Name'].count().sort_values(
        ascending=False
    ).plot(kind='bar', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Meal Types")
    fig, ax = plt.subplots()
    food['Meal_Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
    col1, col2 = st.columns(2)

with col1:
    st.subheader("Food Count by Location")
    fig, ax = plt.subplots()
    food.groupby('Location')['Food_Name'].count().sort_values(
        ascending=False
    ).plot(kind='bar', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Meal Types")
    fig, ax = plt.subplots()
    food['Meal_Type'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
    st.markdown("""
This dashboard provides insights into food donations,
providers, receivers, and claims to help reduce food wastage.
""")
