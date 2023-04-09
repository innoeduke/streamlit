import streamlit as st
import yfinance as yf

# A Complete Guide of yfinance: 
# https://algotrading101.com/learn/yfinance-guide/

st.header('Stock Information Application')

tickerSymbol = st.text_input('Ticker Symbol:', value='NTCT')
tickerData = yf.Ticker(tickerSymbol)
# tickerData.info
df = tickerData.history(interval='1mo', start='2007-01-01', end=None)

st.write(f"""
Shown are the stock price and volume of {tickerData.info['displayName']} \
    ({tickerData.info['fullExchangeName']}: {tickerSymbol})
"""
)

st.subheader('Close Price')
st.line_chart(df[['Close','High']])
st.subheader('Volume')
st.bar_chart(df.Volume)