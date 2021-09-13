import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

# Run in terminal to get an Excel spreadsheet of immediate information of 
# the current top 30 cryptocurrencies.

# Change spreadsheet save path on line 42.

# download from web
url = "https://price.btcfans.com/coin/"
soup = BeautifulSoup(requests.get(url).text, "lxml")

# extract data from webpage
time = soup.find(id="MarketClock").get_text()[5:] # Beijing time
time = time.replace('/', '-')
time = time.replace(':', '.')
time = time.replace(' ', ' @ ')

tags = soup.find_all(class_="table-col col1")[1:31]
prices = [price.get_text().strip() for price in soup.find_all(
    class_="table-col col2")[1:31]]
diffs = [diff.get_text().strip() for diff in soup.find_all(
    class_=re.compile("table-col col4"))[1:31]]
diffs = [("+" + diff) if '-' not in diff else diff for diff in diffs]
deals = [deal.get_text().strip() for deal in soup.find_all(
    class_="table-col col7")[1:31]]

# process tags to make them more readable
names = [tag.find(class_="name").get_text() for tag in tags]
subs = [tag.find(class_="sub").get_text() for tag in tags]
tags = [(name + "(" + sub + ")") for (name, sub) in zip(names, subs)]

# use pandas dataframe object to store data
columns = ["Coin Type", "Price(USD)", "Diff(24hr)", "Deal(24hr)"]
spreadsheet = [[tag, price, diff, deal] for tag, price, diff, deal in zip(
    tags, prices, diffs, deals)]
dataframe = pd.DataFrame(spreadsheet, index=range(1, 31), columns=columns)

# save spreadsheet
path = './' + time + '.xlsx'
dataframe.to_excel(path)
print("Spreadsheet saved to " + path)
