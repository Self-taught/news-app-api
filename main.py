import requests
import streamlit as st

api_key = "654527ebf9044394afafc1eb04005366"

url = ('https://newsapi.org/v2/everything?'
       'q=cryptocurrency, altcoins, bitcoin, ethereum&'  
       'from=2023-03-01&'
       'sortBy=popularity&'
       'apiKey=654527ebf9044394afafc1eb04005366')

# Make request
response = requests.get(url)

# Get a dictionary with data
content = response.json()

# Access the article title and description
for art in content["articles"]:
       st.header(art["title"])
       st.write(art["description"])