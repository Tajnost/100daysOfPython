import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STONKS = "TRJX5OR7TZQSVMJG"
API_KEY_NEWS = "2cb18fd638864fdca68041458fc905d2"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = str(datetime.today().strftime('%Y-%m-%d'))

yesterday = datetime.now() - timedelta(1)
day_before_yesterday = datetime.today() - timedelta(2)

yesterday = str(datetime.strftime(yesterday, '%Y-%m-%d'))
day_before_yesterday = str(datetime.strftime(day_before_yesterday, '%Y-%m-%d'))

print(f"Today's date: {day_before_yesterday}, {yesterday}")
print(f"Today's date: {today}")

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEY_STONKS}'
r = requests.get(url)
data = r.json()

print(data["Time Series (Daily)"][yesterday]["4. close"])
print(data["Time Series (Daily)"][day_before_yesterday]["4. close"])

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

yesterday_closing_price = data["Time Series (Daily)"][yesterday]["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_price = data["Time Series (Daily)"][day_before_yesterday]["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

difference_price = (abs(float(yesterday_closing_price) - float(day_before_yesterday_price)) ) * 100 / float(yesterday_closing_price)
print(difference_price)




#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if difference_price >= 2:
    urlnews = f"https://newsapi.org/v2/everything?q=tesla&from={yesterday_closing_price}&sortBy=publishedAt&apiKey={API_KEY_NEWS}"
    rn = requests.get(urlnews)
    data2 = rn.json()["articles"]
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = data2[:3]

    formatted_articles = [f"{STOCK_NAME}:\n Headline: {data2['title']}. \n Brief: {data2['description']}" for data2 in three_articles]
print(formatted_articles[0])
print(formatted_articles[1])
print(formatted_articles[2])



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

