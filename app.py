import starfishX as sx
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

image = Image.open('logo.png')

st.image(image, width = 250)

st.write("""
# Thai stock price app
""")

# Create get_stock function to pull stock data
def get_stock(stock, startdate='2016-01-01'):

  df = sx.loadHistData(stock, start=startdate,
                      OHLC=True, Volume=True)
  
  return df

stock_symbol = st.text_input("Stock Symbol (ex. AOT, PTT, etc.)", 'AOT')
date = st.selectbox('select startdate', [2010, 2011, 2012, 2013, 2014, 
2015, 2016, 2017, 2018, 2019, 2020])
start_date = f'{date}-01-01'

try:
  df = get_stock(stock=stock_symbol, startdate=start_date)

  st.dataframe(df)

  st.dataframe(df.describe())
  # Stock symbol
  st.write(stock_symbol)

  # Closing Price
  st.write("""
  ## Closing Price
  """)
  st.line_chart(df.CLOSE)

  # Volume Price
  st.write("""
  ## Volume 
  """)
  st.line_chart(df.VOLUME)

  # display income statement
  st.write("""
  ## Income Statement
  """)
  st.dataframe(sx.getIncomeStatement(stock_symbol))

  # display financial ratio
  st.write("""
  ## Financial ratio
  """)
  st.dataframe(sx.getFinanceRatio(stock_symbol))

except:
  st.error('The data of this stock is currently not available')
  st.error('ไม่พบข้อมูล')
