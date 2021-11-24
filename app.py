from bs4 import BeautifulSoup

import requests
import pandas as pd
import numpy as np
import streamlit as st
import base64
import pandas as pd
import time

from datetime import date
from io import BytesIO

page = st.selectbox("Choose your page", ["IMX", "L1 Network Activities", "OpenSea Rarity"])
if page == "IMX":
    url="https://imxflow.com"
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    st.title("Immutable X Marketplace")
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()
    df1 = html_content
    a= df1.split()
    d = pd.DataFrame(columns = ['project','minted', 'holders', 'NFTssold','total sales (USD)'])
    count = 0
    total = 0

    for i in range(len(a)):
        title = ""
        if 'class="coll_name2">' in a[i]:
            for j in range(i, len(a)):
                title += a[j]
                if '</div><div' in a[j]:
                    title += a[j]
                    break
            title =  title[19:]
            index = title.find('</div>')
            d.loc[count, 'project']  = title[:index]
            count +=1
    count = 0

    total = 0

    for i in range(len(a)):
        title = ""
        total = 0
        if 'class="small_desc_label">Minted</div><div' in a[i]:
            title =  a[i+1]
            c = list(title)
            sa = ""
            for i in c:
                if i.isdigit():
                  sa += i
            total += int(sa)
            d.loc[count, 'minted']  = total
            count +=1
    count = 0
    total = 0

    for i in range(len(a)):
        title = ""
        total = 0
        if 'class="small_desc_label">Holders</div><div' in a[i]:
            title =  a[i+1]
            c = list(title)
            sa = ""
            for i in c:
                if i.isdigit():
                  sa += i
            total += int(sa)
            d.loc[count, 'holders']  = total
            count +=1
    count = 0
    total = 0

    for i in range(len(a)):
        title = ""
        total = 0
        if 'class="small_desc_label">Sales</div><div' in a[i]:
            title  = a[i+1]
            c = list(title)
            sa = ""
            for i in c:
                if i.isdigit():
                  sa += i
            total += int(sa)
            d.loc[count, 'NFTssold']  = total
            count +=1
    count = 0

    total = 0

    for i in range(len(a)):
        title = ""
        total = 0
        if 'class="arrow_rank">' in a[i]:
            title =  a[i+1]
            c = list(title)
            sa = ""
            for i in c:
                if i.isdigit():
                  sa += i

            d.loc[count, 'total sales (USD)']  = sa
            count += 1
    st.dataframe(d)
    number = str(len(d))
    st.write("Number of NFT Projects on IMX = " + number)

if page == "L1 Network Activities":
    st.title("Avalanche, Algorand, Fantom, Elrond Network")
    st.write("Avalanche and Fantom has a 2 day delay in their explorer")
    st.write("Algorand's explorer has to be updated 4 months later")
    url = "https://snowtrace.io/chart/tx"

    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find('October 1, 2021')
    end = a.find('Highcharts')
    a = a[start:end]
    a = a.split()
    # avalanche
    d = pd.DataFrame(columns=['blocktime', 'avatxnactivity', 'avanewaddress', 'ftmtxnactivity', 'ftmnewaddress', 'elrondtxnactivity', 'elrondnewaddress', 'algorandtxnactivity', 'algorandnewaddress'])
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

    count = 0
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
    start = a.find('October 1, 2021')
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
    count = 0
    b = ""
    for i in range(len(a)-1):

        if a[i] == 'formattedValue':
            b = a[i + 2]
            c = list(b)
            sa = ""
            for i in c:
                if i.isdigit():
                    sa += i
            d.loc[count, 'ftmtxnactivity'] = int(sa)
            count += 1

    d.loc[0, 'blocktime'] = '1 June 2020'

# fantom
    #elrond

    url = "https://data.elrond.com/latestcomplete/transactionshistorical/transactions/count_24h"

    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.prettify()

    start = a.find('"time":"2021-10-01T00:00:00.000Z"')
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

    start = a.find('"time":"2021-10-01T00:00:00.000Z"')
    b = a[start:].split("time")

    count = 0
    total = 0
    initial = 799298
    temp = 0
    for i in range(1, len(b)):
        l = b[i][35:]
        c = l
        sa = ""

        for j in c:
            if j.isdigit():
                sa += str(j)

        if count ==0:

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

    start = a.find('"time-start":1632960000')
    a = a[start:].split("time")


    count = 0
    total = 0



    count = 0
    for i in range(2, len(a), 2):
        c = list(a[i])
        sa = ""
        l = a[i][29:]
        for i in range(len(l)):
            if l[i].isdigit():
                sa += l[i]
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

    start = a.find('"time-start":1632960000')
    a = a[start:].split("time")

    initial = 13605221
    count = 0
    before = 0
    for i in range(2, len(a), 2):
        c = list(a[i])
        sa = ""
        l = a[i][31:]
        for j in range(len(l)):
            if l[j].isdigit():
                sa += l[j]
            else:
                break
        if i == 2:

            d.loc[count, 'algorandnewaddress'] = int(sa) - initial
            before = int(sa)
        else:

            d.loc[count, 'algorandnewaddress'] = int(sa) - before
            before = int(sa)
        count += 1

    d


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


    df = d# your dataframe
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)


    d = d.dropna()
    index = d['blocktime']

    df =d[['avanewaddress', 'ftmnewaddress', 'elrondnewaddress', 'algorandnewaddress']].dropna()
    df = df.set_index(index)
    st.write("New Daily Addresses from 1 October 2021")
    st.line_chart(df)

    df = d[['avatxnactivity', 'ftmtxnactivity', 'elrondtxnactivity','algorandtxnactivity']].dropna()
    df = df.set_index(index)
    st.write("Daily Transaction Activity from 1 October 2021")
    st.line_chart(df)

if page == "OpenSea Rarity":

    # to run streamlit run
    collection = st.sidebar.text_input("Collection")
    st.header(collection)
    token = st.sidebar.text_input("Token")
    count1 = st.sidebar.number_input("count")

    params = {}

    if collection:
        params['collection'] = collection
    if token:
        params['token_ids'] = token

    try:
        r = requests.get("https://api.opensea.io/api/v1/assets", params=params)
    except:
        st.write("You printed wrongly")

    response = r.json()
    asset_list = []
    try:
        for asset in response["assets"]:
            asset_rarity = 1

            for trait in asset['traits']:
                trait_rarity = trait['trait_count'] / count1
                asset_rarity *= trait_rarity

                price = float(asset['sell_orders'][0]['base_price']) * 0.000000000000000001

            asset_rarity *= 10 ** 7
            value = asset_rarity * price
            asset_list.append([asset['token_id'], asset_rarity, price, value])
            # findset_list.append(float(trait_count))
        # columns=['rarity score', 'price'])
        df = pd.DataFrame(asset_list, columns=['token_id', 'rarity score', 'price', 'value'])
        st.write(df)

    except:
        st.write("Collection : pudgypenguins from https://opensea.io/collection/pudgypenguins\n")
        st.write("Ensure token has not been bought before")
