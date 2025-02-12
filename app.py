import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import numpy as np

# Streamlit App Title
st.set_page_config(page_title="Nifty 50 Support & Resistance", layout="wide")
st.title("📊 Automated Support & Resistance Detection System")

# Select stock symbol (default: Nifty 50)
ticker = st.text_input("Enter Stock Ticker (Default: ^NSEI for Nifty 50)", "^NSEI")

# Fetch stock data
def get_stock_data(ticker, period="60d"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    data.reset_index(inplace=True)
    return data

data = get_stock_data(ticker)

# Ensure data is available
if data.empty:
    st.error("No data available for the given stock ticker. Please check and try again.")
    st.stop()

# Support & Resistance Detection Functions
def is_support(data, i):
    return data['Low'][i] < data['Low'][i - 1] and data['Low'][i] < data['Low'][i + 1]

def is_resistance(data, i):
    return data['High'][i] > data['High'][i - 1] and data['High'][i] > data['High'][i + 1]

def is_far_from_levels(levels, price, threshold=0.005):
    return np.sum([abs(price - level) < threshold * price for level in levels]) == 0

# Detecting Support & Resistance Levels
support_levels = []
resistance_levels = []

for i in range(1, len(data) - 1):
    if is_support(data, i):
        price = data['Low'][i]
        if is_far_from_levels(support_levels, price):
            support_levels.append(price)
    elif is_resistance(data, i):
        price = data['High'][i]
        if is_far_from_levels(resistance_levels, price):
            resistance_levels.append(price)

# Create Candlestick Chart
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=data['Date'],
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close'],
    name='Candlestick'
))

# Plot Support Levels
for support in support_levels:
    fig.add_hline(y=support, line=dict(color="green", dash="dash"), annotation_text=f"Support: {support:.2f}")

# Plot Resistance Levels
for resistance in resistance_levels:
    fig.add_hline(y=resistance, line=dict(color="red", dash="dash"), annotation_text=f"Resistance: {resistance:.2f}")

# Chart Layout
fig.update_layout(
    title=f"{ticker} Support & Resistance Levels",
    xaxis_title="Date",
    yaxis_title="Price (INR)",
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display Data Table
st.subheader("📜 Latest Stock Data")
st.dataframe(data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].tail(30))
