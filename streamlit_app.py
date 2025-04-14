import streamlit as st
import pandas as pd
import requests

st.title("🕵️ Insider Trade Tracker")

url = "https://senatetradesapi.caydel.com/trades?limit=20"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["results"])
st.subheader("Recent Trades by Senators")
st.dataframe(df[["senator", "ticker", "transaction_type", "transaction_date", "amount"]])
