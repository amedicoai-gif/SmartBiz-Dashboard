import pandas as pd
import streamlit as st
import plotly.express as px

# Load sample data
data = pd.read_csv("data/sales_data.csv")

st.title("SmartBiz-Dashboard Demo")
st.markdown("Interactive Business Analytics Dashboard (Demo)")

# Filter by Product
product = st.selectbox("Select Product", data['Product'].unique())
filtered_data = data[data['Product'] == product]

# Show table
st.subheader("Sales Data")
st.dataframe(filtered_data)

# Revenue over time chart
st.subheader("Revenue Over Time")
fig = px.line(filtered_data, x="Date", y="Revenue", title=f"{product} Revenue Over Time")
st.plotly_chart(fig)

# Units Sold chart
st.subheader("Units Sold Over Time")
fig2 = px.bar(filtered_data, x="Date", y="Units_Sold", title=f"{product} Units Sold Over Time")
st.plotly_chart(fig2)
