import streamlit as st
from nlp import text_clf
from functions import html_result, html_title

st.markdown(html_title("What are you currently thinking?"), unsafe_allow_html=True)

user_input = st.text_input(label="What are you currently thinking?",
                           label_visibility="collapsed",
                           placeholder="Write a word or a sentence here")

if user_input:
    result = text_clf.predict([user_input])[0]
    emoji = "&#128528;"
    emojis = ["&#128522;", "&#128528;", "&#128528;"]
    sentiments = ["positive", "neutral", "negative"]

    for i in range(0, len(sentiments)):
        if sentiments[i] == result:
            emoji = emojis[i]

    st.markdown(html_result(result, emoji), unsafe_allow_html=True)
