import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Food Wastage Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Reduce top and bottom spacing
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Load CSV files
provider = pd.read_csv("providers.csv")
receivers = pd.read_csv("receivers.csv")
claims = pd.read_csv("claims.csv")
food = pd.read_csv("food_list.csv")

# Title
st.title("🍲 Food Wastage Management Dashboard")

# KPI Cards
k1, k2, k3, k4 = st.columns(4)

k1.metric("Providers", len(provider))
k2.metric("Receivers", len(receivers))
k3.metric("Food Items", len(food))
k4.metric("Claims", len(claims))

st.markdown("---")

# First Row
col1, col2 = st.columns(2)

with col1:
    st.subheader("Provider Types")

    fig, ax = plt.subplots(figsize=(4, 2))
    provider['Type'].value_counts().plot(
        kind='line',
        marker='o',
        ax=ax
    )
    plt.xticks(rotation=20, fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    st.subheader("Receiver Types")

    fig, ax = plt.subplots(figsize=(4, 2))
    receivers['Type'].value_counts().plot(
        kind='bar',
        ax=ax
    )
    plt.xticks(rotation=20, fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)

# Second Row
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 5 Providers")

    provider_food = pd.merge(food, provider, on="Provider_ID")

    donation = (
        provider_food.groupby('Name')['Quantity']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    fig, ax = plt.subplots(figsize=(4, 2))
    donation.plot(kind='barh', ax=ax)
    ax.set_xlabel("Quantity")
    ax.set_ylabel("")
    plt.tight_layout()
    st.pyplot(fig)

with col4:
    st.subheader("Meal Types")

    fig, ax = plt.subplots(figsize=(4, 2))
    food['Meal_Type'].value_counts().plot(
        kind='bar',
        ax=ax
    )
    plt.xticks(rotation=20, fontsize=8)
    plt.tight_layout()
    st.pyplot(fig)

st.caption(
    "Dashboard showing insights into food donations, providers, receivers and claims."
)
