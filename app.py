from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import streamlit as st
import base64
import pandas as pd
import time
from datetime import date
from datetime import datetime, timedelta
import plotly.express as px
from io import BytesIO
import tweepy
from PIL import Image
import PIL
import io
import requests
import sys
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
from textblob import TextBlob
import re

st.title("Surfacing Data Points")
page = st.selectbox("Choose your page", ["L1/L2 Network Activities", "NFT Marketplaces", "Twitter Verse", "Newsroom"])


if page == "NFT Marketplaces":
  

    import pandas as pd
    from selenium import webdriver
    import os
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    st.title('Vulcan Forged Unique Players')
    d = pd.DataFrame(columns = ['ForgedArena','Berserk', 'VulcanVerse'])
    driver.get('https://dappradar.com/v2/api/dapp/vulcanforged/games/forge-arena/chart/all?currency=USD')  
    page_source = driver.page_source
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source)
    a = str(soup)
    a = a.split()
    l = a[4]
    x = l.find('data')
    end = l.find('Transactions')
    l1 = l[x:end]
    end2 = l1.find('name')
    l1 = l1[5:end2][::-1][5:]

    number = 0 
    usergrowth = []
    count = 0 
    s = " "
    for i in range(len(l1)): 
        number = 0 
        if l1[i].isdigit(): 
            s += l1[i]
        elif l1[i] == ',':
            s = s[::-1]
            usergrowth.append(s)

            d.loc[count, 'ForgedArena'] = s
            s = ""
            count += 1

    d.loc[0,'ForgedArena']= 8 
    
    
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://dappradar.com/v2/api/dapp/vulcanforged/games/berserk-vulcanites-unleashed/chart/all?currency=USD')  
    page_source = driver.page_source
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source)
    a = str(soup)
    a = a.split()
    l = a[4]
    x = l.find('data')
    end = l.find('Transactions')
    l1 = l[x:end]
    end2 = l1.find('name')
    l1 = l1[5:end2][::-1][5:]

    number = 0 
    usergrowth = []
    count = 2 
    for i in range(len(l1)): 
        number = 0 
        if l1[i].isdigit(): 
            s += l1[i]
        elif l1[i] == ',':
            s = s[::-1]
            usergrowth.append(s)
            d.loc[count, 'Berserk'] = s
            s = ""
            count += 1

    d.loc[0, 'Berserk'] = 0 
    d.loc[1, 'Berserk'] = 0 
    d.loc[2, 'Berserk'] = 109 



    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://dappradar.com/v2/api/dapp/vulcanforged/games/vulcanverse/chart/all?currency=USD')  
    page_source = driver.page_source
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source)
    a = str(soup)
    a = a.split()
    l = a[4]
    x = l.find('data')
    end = l.find('Transactions')
    l1 = l[x:end]
    end2 = l1.find('name')
    l1 = l1[5:end2][::-1][5:]

    number = 0 
    usergrowth = []
    count = 3 
    for i in range(len(l1)): 
        number = 0 
        if l1[i].isdigit(): 
            s += l1[i]
        elif l1[i] == ',':
            s = s[::-1]
            d.loc[count, 'VulcanVerse'] = s
            s = ""
            count += 1


    d.loc[0, 'VulcanVerse'] = 0 
    d.loc[1, 'VulcanVerse'] = 0 

    d.loc[2, 'VulcanVerse'] = 0 
    d.loc[3, 'VulcanVerse'] = 124
    d
    df = d.dropna()
    
    st.write('Over the past week:')
    maximum = len(d)
    weekly = d.loc[ maximum - 7: maximum, :]
    weekly
    
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data


    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        val = to_excel(df)
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="VulcanVerse.xlsx">Download csv file</a>'  # decode b'abc' => abc


    df = d  # your dataframe
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    
    st.line_chart(df)
    
    
    
    url="https://cardsunchained.com/?pstat=1"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()



    start = a.find('data:')
    l = a[start:].split()[16:17]
    df = pd.DataFrame(columns = ['date','uniqueplayers'])
    count = 0
    number = ''
    l = str(l)[2:-1]
    history = 60 
    for i in range(len(l)): 
        if l[i].isdigit(): 
            number += l[i]
        else: 
            df.loc[count, 'uniqueplayers'] = int(number) 
            df.loc[count, 'date'] =str(datetime.now()     - timedelta(days=history))[:10]
            number = ''
            count += 1
            history -=1


    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        val = to_excel(df)
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="GodsUnchained.xlsx">Download csv file</a>'  # decode b'abc' => abc


    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    st.title("Gods Unchained Unique Players")
    st.write("Past 2 months")
    df
    st.line_chart(df)
    


if page == "L1/L2 Network Activities":
    st.title("L1/2 Network")

    st.write("Networks supported: Ethereum, Terra, Avalanche, Algorand, Fantom, Elrond, Polygon, Arbitrum")
    d = pd.DataFrame(
        columns=['blocktime', 'polytxnactivity', 'polynewaddress', 'arbitxnactivity',
                 'arbinewaddress', 'avatxnactivity', 'avanewaddress', 'ftmtxnactivity', 'ftmnewaddress',
                 'elrondtxnactivity',
                 'elrondnewaddress', 'algorandtxnactivity', 'algorandnewaddress'])
    st.write("Today's date: " + str(date.today()) )
    history = date.today() - pd.DateOffset(months=3)
    st.write("Dataset follows a 3 month window. **Live Data Feeds from Explorers**" )
    st.write("Delay of up to 1 day")
   
    history = str(history)[:10]
    url = "https://snowtrace.io/chart/tx"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()
    months = [
              "January",
              "Febuary",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]

    dd = history[8:]
    if dd[0] == '0':
        dd = dd[1]
    y = history[:4]
    mm = history[5:7]
    if mm[0] == '0':
        mm = mm[1]
    mm = int(mm)
    mo  = mm
    mm = months[mm -1]
    hist = mm + " " + dd + "," + " " + y
    start = a.find(hist) + 1
    end = a.find('Highcharts')
    a = a[start:end]
    a = a.split()
    # avalanche
    count = 0
    total = 0

    for i in range(len(a)):
        if a[i] == 'newaddress':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i

            d.loc[count, 'avanewaddress'] = int(sa)
            count += 1

    count = 1
    skip = 0 
    b = ""
    for i in range(len(a)):
      
        if a[i] == 'formattedValue':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'avatxnactivity'] = int(sa)
            count += 1
    count = 0

    url = "https://ftmscan.com/chart/tx"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()
    start = a.find(hist)
    end = a.find('Highcharts')
    a = a[start:end]
    a = a.split()

    count = 0
    total = 0

    for i in range(len(a)):
        if a[i] == 'newaddress':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            total = int(sa)
            d.loc[count, 'ftmnewaddress'] = total
            count += 1
    count = 1
    b = ""
    for i in range(len(a) - 1):

        if a[i] == 'formattedValue':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'ftmtxnactivity'] = int(sa)
            count += 1

    # fantom
    # elrond

    url = "https://data.elrond.com/latestcomplete/transactionshistorical/transactions/count_24h"

    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find('"time":"' + history+ 'T00:00:00.000Z"')
    b = a[start:].split("time")
    count = 0
    total = 0

    for i in range(1, len(b)):
        l = b[i][35:]
        c = l
        sa = ""
        for j in c:
            if j.isdigit():
                sa += str(j)
        d.loc[count, 'elrondtxnactivity'] = int(sa)
        count += 1
    url = "https://data.elrond.com/latestcomplete/accountshistorical/accounts/count"
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find('"time":"' + history+ 'T00:00:00.000Z"')
    b = a[start:].split("time")

    count = 1
    total = 0
    l = b[1][35:]
    c = l
    sa = ""

    for j in c:
        if j.isdigit():
            sa += str(j)
    initial = int(sa)

    temp = 0
    for i in range(2, len(b)):
        l = b[i][35:]
        c = l
        sa = ""

        for j in c:
            if j.isdigit():
                sa += str(j)

        if count == 0:

            d.loc[count, 'elrondnewaddress'] = int(sa) - initial
            temp = int(sa)
        else:

            d.loc[count, 'elrondnewaddress'] = int(sa) - temp
            temp = int(sa)
        count += 1
    count = 0
    total = 0

    for i in range(1, len(b)):
        l = b[i][3:13]

        d.loc[count, 'blocktime'] = l
        count += 1

    import datetime

    url = "https://indexer.algoexplorerapi.io/stats/v2/transactions/count?time-start=1621983374&interval=1D"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()
    #converting to epoch
    epoch = datetime.datetime(int(y), int(mo), int(dd),0,0).strftime('%s')

    time = int(epoch) 

    start = a.find('"time-start":' + str(time))
    
    a = a[start:].split("time")

    l = a[2][29:]
   
    for j in range(len(l)):
        if l[j].isdigit():
            sa += l[j]
        else:
            break
    initial = int(sa)


    count = 1
    before = 0
    for i in range(4, len(a), 2):
        c = list(a[i])
        sa = ""
        l = a[i][29:]
        for j in range(len(l)):
            if l[j].isdigit():
                sa += l[j]
            else:
                break
        d.loc[count, 'algorandtxnactivity'] = int(sa)
        count += 1

    url = "https://indexer.algoexplorerapi.io/stats/v2/accounts/balances?time-start=1621983259&interval=1D"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find('"time-start":' + str(time))
    a = a[start:].split("time")
    l = a[2][:]
    for j in range(20,len(l)):
        if l[j].isdigit():
            sa += l[j]
        else:
            break
    initial = int(sa)

    count = 1
    before = 0
    for i in range(4, len(a), 2):
        c = list(a[i])
        sa = ""
        l = a[i][31:]
        for j in range(len(l)):
            if l[j].isdigit():
                sa += l[j]
            else:
                break
        if i == 4:

            d.loc[count, 'algorandnewaddress'] = int(sa) - initial
            before = int(sa)
        else:

            d.loc[count, 'algorandnewaddress'] = int(sa) - before
            before = int(sa)
        count += 1

    # polyscan

    url = "https://polygonscan.com/chart/tx"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find(hist)
    end = a.find('Highcharts')

    a = a[start:end].split()

    count = 1
    total = 0

    for i in range(14, len(a)):
        if a[i] == 'newaddress':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'polynewaddress'] = int(sa)
            count += 1

    count = 1
    b = ""
    for i in range(len(a)):

        if a[i] == 'formattedValue':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'polytxnactivity'] = int(sa)
            count += 1
    count = 1

    # arbiscan
    url = "https://arbiscan.io/chart/tx"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find(hist)
    end = a.find('Highcharts')
    a = a[start:end].split()

    count = 1
    total = 0

    for i in range(14, len(a)):
        if a[i] == 'newaddress':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'arbinewaddress'] = int(sa)
            count += 1

    count = 1
    b = ""
    for i in range(len(a)):

        if a[i] == 'formattedValue':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'arbitxnactivity'] = int(sa)
            count += 1
    count = 0
    
    
        #stops here

    
    d= d.drop(index = 0 )
    d = d.drop(index = 1)
    d = d.drop(index = 2)
    
    d

    st.write('Over the past week:')
    maximum = len(d)
    weekly = d.loc[ maximum - 7: maximum, :]
    
    weekly
    

    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data


    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        val = to_excel(df)
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="L1Networks.xlsx">Download csv file</a>'  # decode b'abc' => abc


    df = d  # your dataframe
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    
    d = d.dropna()
    index = d['blocktime']
    
    
    st.write("**Past 2 Weeks**")
    
    st.write("New Addresses")
    df = d [[ 'polynewaddress', 'arbinewaddress', 'avanewaddress', 'ftmnewaddress', 'elrondnewaddress',
            'algorandnewaddress']].dropna()
    df = df.set_index(index)
    
    st.line_chart(df[77:])
    
    st.write("Txn Activity")
    df =  d [['ethtxnactivity', 'terratxnactivity', 'polytxnactivity', 'arbitxnactivity', 'avatxnactivity', 'ftmtxnactivity', 'elrondtxnactivity',
            'algorandtxnactivity']].dropna()
    df = df.set_index(index)
 
    st.line_chart(df[77:])
    
    
    st.write("**From** " + hist)
    df = d[[ 'polynewaddress', 'arbinewaddress', 'avanewaddress', 'ftmnewaddress', 'elrondnewaddress',
            'algorandnewaddress']].dropna()
    df = df.set_index(index)
    st.write("New Addresses")
    st.line_chart(df)

    df = d[['ethtxnactivity', 'terratxnactivity', 'polytxnactivity', 'arbitxnactivity', 'avatxnactivity', 'ftmtxnactivity', 'elrondtxnactivity',
            'algorandtxnactivity']].dropna()
    df = df.set_index(index)
    st.write("Txn Activity")
    st.line_chart(df)

    st.write("**Without Polygon**")
    df = d[['arbinewaddress', 'avanewaddress', 'ftmnewaddress', 'elrondnewaddress', 'algorandnewaddress']].dropna()
    df = df.set_index(index)
    st.write("New Addresses")
    st.line_chart(df)

    df = d[['ethtxnactivity', 'terratxnactivity','arbitxnactivity', 'avatxnactivity', 'ftmtxnactivity', 'elrondtxnactivity', 'algorandtxnactivity']].dropna()
    df = df.set_index(index)
    st.write("Txn Activity")
    st.line_chart(df)
    
    

if page == "Twitter Verse":

    consumerKey =   'sXxEobwFV4b1oEaigeF6sUsAb'# confidential
    consumerSecret = '5R0I1UNItyvda96brk2aN3E1WMdoprbIpiVLTgoerOmDoOYTI7' # confidential
    accessToken =  '1444264136666353667-iHg1KKdK6Zowd7SlbiHkGcclLLzZ6B'# confidential
    accessTokenSecret = 'HzdZCnP8TBotJSGVo4L7fk644OTHR6AgjBImxcaYHKcnw' # confidential

    # Create the authentication object
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

    # Set the access token and access token secret
    authenticate.set_access_token(accessToken, accessTokenSecret)

    # Creating the API object while passing in auth information
    api = tweepy.API(authenticate, wait_on_rate_limit=True)

    
    consumer_key =   'sXxEobwFV4b1oEaigeF6sUsAb'# confidential
    consumer_secret = '5R0I1UNItyvda96brk2aN3E1WMdoprbIpiVLTgoerOmDoOYTI7' # confidential
    access_token =  '1444264136666353667-iHg1KKdK6Zowd7SlbiHkGcclLLzZ6B'# confidential
    access_token_secret = 'HzdZCnP8TBotJSGVo4L7fk644OTHR6AgjBImxcaYHKcnw' # confidential

    # creating the authentication object, setting access token and creating the api object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    ####################################################################################
    #                         Function to retrieve the tweets                          #
    ####################################################################################


    def get_tweets(user_name, tweet_count):
        tweets_list = []
        img_url = ""
        name = ""

        for tweet in api.user_timeline(
            id=user_name, count=100, tweet_mode="extended"
        ):
            tweets_dict = {}

            tweets_dict["tweet"] = tweet.full_text

            tweets_list.append(tweets_dict)

        return tweets_list


    ####################################################################################
    #       Function to prepare the data for word cloud and sentiment analysis         #
    ####################################################################################

    extra_stopwords = ["The", "It", "it"]


    def prep_data(tweet):
        # cleaning the data
        tweet = re.sub("https?:\/\/\S+", "", tweet)  # replacing url with domain name
        tweet = re.sub("#[A-Za-z0–9]+", " ", tweet)  # removing #mentions
        tweet = re.sub("#", " ", tweet)  # removing hash tag
        tweet = re.sub("\n", " ", tweet)  # removing \n
        tweet = re.sub("@[A-Za-z0–9]+", "", tweet)  # removing @mentions
        tweet = re.sub("RT", "", tweet)  # removing RT
        tweet = re.sub("^[a-zA-Z]{1,2}$", "", tweet)  # removing 1-2 char long words
        tweet = re.sub("\w*\d\w*", "", tweet)  # removing words containing digits
        for word in extra_stopwords:
            tweet = tweet.replace(word, "")

        # lemmitizing
        lemmatizer = WordNetLemmatizer()
        new_s = ""
        for word in tweet.split(" "):
           new_s += word

        return new_s


    ####################################################################################
    #           Function to create the word cloud based on tweets data                 #
    ####################################################################################


    def wordcloud(clean_tweet):
        wordcloud_words = " ".join(clean_tweet)
        wordcloud = WordCloud(
            height=300, width=500, background_color="white", random_state=500,
        ).generate(wordcloud_words)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig("cloud.jpg")
        img = Image.open("cloud.jpg")
        return img




    #####################################################################################
    #                                  Main App                                         #
    #####################################################################################

    
    st.title("Twitter Verse")

    raw_text = st.text_area("Enter the exact twitter handle (without @ and space) eg. defiMoon,Arthur_0x,EnterDAO    Error if wrongly recorded")
    l1 = raw_text.split(',')
    tweet_df = pd.DataFrame(columns=[ 'tweet'])
    count = 0
    for i in range(len(l1)):
        posts = api.user_timeline(screen_name=l1[i], count=100, exclude_replies=True, lang="en", tweet_mode="extended")
        for tweet in posts[:100]:

            tweet_df.loc[count, 'tweet'] = tweet.full_text
            count += 1

            # calling the function to prep the data
    tweet_df["clean_tweet"] = tweet_df["tweet"].apply(prep_data)

            # calling the function to create the word cloud
    img = wordcloud(tweet_df["clean_tweet"])

    st.image(img)
   
    df = pd.DataFrame(columns = ['name', 'time', 'favourite_count', 'retweet_count', 'tweet'])
    count = 0
    for i in range(len(l1)):
      posts = api.user_timeline(screen_name=l1[i], count=100, exclude_replies=True,lang="en", tweet_mode="extended")
      for tweet in posts[:10]:
        df.loc[count, 'name'] = l1[i]
        df.loc[count, 'time'] = str(tweet.created_at)
        df.loc[count, 'favourite_count'] = tweet.favorite_count
        df.loc[count, 'retweet_count'] = tweet.retweet_count
        df.loc[count, 'tweet'] = tweet.full_text
        count += 1

    st.write(df)
    
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        processed_data = output.getvalue()
        return processed_data


    def get_table_download_link(df):
        """Generates a link allowing the data in a given panda dataframe to be downloaded
        in:  dataframe
        out: href string
        """
        val = to_excel(df)
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="Twitter.csv">Download csv file</a>'  # decode b'abc' => abc

    st.markdown(get_table_download_link(df), unsafe_allow_html=True)




if page == "Newsroom":
    consumerKey =   'sXxEobwFV4b1oEaigeF6sUsAb'# confidential
    consumerSecret = '5R0I1UNItyvda96brk2aN3E1WMdoprbIpiVLTgoerOmDoOYTI7' # confidential
    accessToken =  '1444264136666353667-iHg1KKdK6Zowd7SlbiHkGcclLLzZ6B'# confidential
    accessTokenSecret = 'HzdZCnP8TBotJSGVo4L7fk644OTHR6AgjBImxcaYHKcnw' # confidential

    # Create the authentication object
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

    # Set the access token and access token secret
    authenticate.set_access_token(accessToken, accessTokenSecret)

    # Creating the API object while passing in auth information
    api = tweepy.API(authenticate, wait_on_rate_limit=True)
    st.title("Newsroom")
    raw_text = 'ElrondNetwork, avalancheavax, terra_money, Algorand, Polkadot, TheDopeWars, SIPHERxyz, Immutable'
    l1 = raw_text.split(',')

    df = pd.DataFrame(columns=['name', 'time', 'tweet'])
    count = 0
    for i in range(len(l1)):
        posts = api.user_timeline(screen_name=l1[i], count=100, exclude_replies=True, lang="en", tweet_mode="extended")
        for tweet in posts[:10]:
            df.loc[count, 'name'] = l1[i]
            df.loc[count, 'time'] = str(tweet.created_at)[:19]
            df.loc[count, 'tweet'] = tweet.full_text
            count += 1
    df1 = df.sort_values(by='time', ascending=False)
    df1 = df1.reset_index()
    df1 = df1.drop(columns='index')


    for i in range(len(df1)):
        st.write(df1.loc[i,:'time'])
        string = df1.loc[i, 'tweet']
        st.write(string)
