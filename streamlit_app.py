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

# 1. Provider Types Distribution
st.subheader("1. Provider Types Distribution")
fig, ax = plt.subplots()
provider['Type'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 2. Receiver Types Distribution
st.subheader("2. Receiver Types Distribution")
fig, ax = plt.subplots()
receivers['Type'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 3. Provider Types Alphabetical
st.subheader("3. Provider Types (Alphabetical)")
fig, ax = plt.subplots()
provider['Type'].value_counts().sort_index().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 4. Providers in Saraland
st.subheader("4. Providers in Saraland")
saraland_provider = provider[provider['City'] == "Saraland"]
st.write(saraland_provider)

# 5. Claims per Receiver
st.subheader("5. Claims per Receiver")
fig, ax = plt.subplots()
claims.groupby('Receiver_ID')['Claim_ID'].count().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 6. Food Count by Location
st.subheader("6. Food Count by Location")
fig, ax = plt.subplots()
food.groupby('Location')['Food_Name'].count().sort_values(ascending=False).plot(kind='bar', ax=ax)
st.pyplot(fig)

# 7. Total Food Quantity
st.subheader("7. Total Quantity of Food")
st.write(food['Quantity'].sum())

# 8. Food Types Distribution
st.subheader("8. Food Types Distribution")
fig, ax = plt.subplots()
food['Food_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
st.pyplot(fig)

# 9. Claims per Food Item
st.subheader("9. Claims per Food Item")
claims_food = pd.merge(claims, food, on="Food_ID")
fig, ax = plt.subplots()
claims_food.groupby('Food_Name')['Claim_ID'].count().sort_values(ascending=False).plot(kind='bar', ax=ax)
st.pyplot(fig)

# 10. Successful Claims per Provider
st.subheader("10. Successful Claims per Provider")
claims_provider = pd.merge(claims, food, on="Food_ID")
claims_provider = pd.merge(claims_provider, provider, on="Provider_ID")
fig, ax = plt.subplots()
claims_provider.groupby('Name')['Claim_ID'].count().sort_values(ascending=False).plot(kind='bar', ax=ax)
st.pyplot(fig)

# 11. Average Claim ID by Status
st.subheader("11. Average Claim ID by Status")
fig, ax = plt.subplots()
claims.groupby('Status')['Claim_ID'].mean().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 12. Meal Types
st.subheader("12. Meal Types")
fig, ax = plt.subplots()
food['Meal_Type'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)

# 13. Quantity Donated per Provider
st.subheader("13. Quantity Donated per Provider")
provider_food = pd.merge(food, provider, on="Provider_ID")
fig, ax = plt.subplots()
provider_food.groupby('Name')['Quantity'].sum().sort_values(ascending=False).plot(kind='bar', ax=ax)
st.pyplot(fig)

# 14. Average Quantity Claimed per Receiver
st.subheader("14. Average Quantity Claimed per Receiver")
claims_food_receiver = pd.merge(claims, food, on="Food_ID")
claims_food_receiver = pd.merge(claims_food_receiver, receivers, on="Receiver_ID")
fig, ax = plt.subplots()
claims_food_receiver.groupby('Name')['Quantity'].mean().sort_values(ascending=False).plot(kind='bar', ax=ax)
st.pyplot(fig)

