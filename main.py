import requests
import streamlit as st
import smtplib, ssl

def send_email(message, receiver):
    host = "smtp.gmail.com"
    port = 465

    username = "looftee08@gmail.com"
    password = "fclhtgzwyjwbnxar"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


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

# Get the list of news articles on your mail
with st.form(key="form"):
    receiver_email = st.text_input("Type your email address", key="receiver_email")
    button = st.form_submit_button("Get email")
    if button:
        body = ""
        a = 0
        for art in content["articles"]:
            if a <= 10:
                body = body + art["title"] + "\n" + art["description"] + 2*"\n"

        body = body.encode("utf-8")
        send_email(body, receiver_email)
        st.info("Email Sent")
# Access the article title and description
a = 0
for art in content["articles"]:
    if a <= 10:
        st.header(art["title"])
        st.write(art["description"])
        st.markdown(f"[Source]({art['url']})")
        a += 1
    else:
        break
