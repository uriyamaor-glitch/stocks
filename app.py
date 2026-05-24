import streamlit as st
import yfinance as yf

st.title("הבורסה שלי 🚀")
ticker = st.selectbox("בחר מניה:", ["AAPL", "TSLA", "NVDA", "MSFT"])
data = yf.Ticker(ticker).history(period="1mo")
st.line_chart(data.Close)
