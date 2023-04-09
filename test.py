import streamlit as st
import yfinance as yf

st.header('Stock Information Application')

tickerSymbol = st.text_input('Ticker Symbol:')
tickerData = yf.Ticker(tickerSymbol)
st.write(f"""
    Company Name: {tickerData.info['displayName']}
""")

df = tickerData.history(interval='1mo',start='2010-02-16', end=None)

st.subheader('Price')
st.line_chart(df[['Low','High']])
st.subheader('Volume')
st.bar_chart(df.Volume)