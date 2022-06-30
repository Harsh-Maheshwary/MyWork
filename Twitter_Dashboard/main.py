import streamlit as st
import pandas as pd
import plotly as px
import requests
import tweepy
import numpy as np
import pytwits
import requests 
import psycopg2, psycopg2.extras
import plotly.graph_objects as go
import config

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


# The Sidebar Layout with elements

st.sidebar.title("Options")

option = st.sidebar.selectbox(
     'Which Dashboard would you like to see?',
     ('Twitter', 'Wall Street Bets','StockTwits'  ,'Chart', 'Pattern'),3)

st.sidebar.write('You selected:', option)

st.header(option)

#if option == 'Twitter':
#    for username in config.TWITTER_USERNAMES:
#        st.write(username)
        
 #       user = api.get_user(username)
      #  user = api.get_user(username)
      #  tweets = api.user_timeline(username)

       # st.subheader(username)
       # st.image(user.profile_image_url)
        
       # for tweet in tweets:
       #     if '$' in tweet.text:
        #        words = tweet.text.split(' ')
         #       for word in words:
          #          if word.startswith('$') and word[1:].isalpha():
           #             symbol = word[1:]
            #            st.write(symbol)
             #           st.write(tweet.text)
              #          st.image(f"https://finviz.com/chart.ashx?t={symbol}")


if option == 'Wall Street Bets':
    st.subheader("This is the Wall Street Bets Logic")
    cursor.execute("""
        SELECT * FROM TwitterMentions LIMIT 10
    """)
    rows = cursor.fetchall
    st.write(rows)


if option == 'Pattern':
    st.subheader("This is the Pattern")




if option == "Chart":
    symbol = st.sidebar.text_input("Symbol", value='MSFT', max_chars=None, key=None, type='default')

    data = pd.read_sql("""
        select date(day) as day, open, high, low, close
        from daily_bars
        where stock_id = (select id from stock where UPPER(symbol) = %s) 
        order by day asc""", connection, params=(symbol.upper(),))

    st.subheader(symbol.upper())

    fig = go.Figure(data=[go.Candlestick(x=data['day'],
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close'],
                    name=symbol)])

    fig.update_xaxes(type='category')
    fig.update_layout(height=700)

    st.plotly_chart(fig, use_container_width=True)

    st.write(data)




if option == 'StockTwits':
    symbol = st.sidebar.text_input("Symbol", value='AAPL', max_chars=10) # accepts user input Symbol to search

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json") # user input symbol is requested
    if r.ok:
        data = r.json()
    #st.write(data)

        for message in data['messages']:
            st.image(message['user']['avatar_url'])
            st.write(message['user']['username'])
            st.write(message['created_at'])
            st.write(message['body'])
    else:
        st.write("Please enter valid symbol!")

    