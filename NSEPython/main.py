import nsepython
import pandas
import streamlit as st

from nsepython import *
positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
df = pd.DataFrame(positions['data'])

#print(df)

print(nse_optionchain_scrapper('RIL'))

oi_data, ltp, crontime = oi_chain_builder("RELIANCE","latest","full")
print(oi_data)
print(ltp)
print(crontime)