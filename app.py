import streamlit as st
from nlp import text_clf

question = st.title("What are you currently thinking?")

title = st.text_input(label="What are you currently thinking?", 
                      label_visibility="collapsed", 
                      placeholder="Enter text here")
                      
if title:
    result = text_clf.predict([title])[0]
    emoji = ":neutral_face:"
    emojis = [":blush:", ":neutral_face: ", ":unamused:"]
    sentiments = ["positive", "neutral", "negative"]

    for i in range(0, len(sentiments)):
        if sentiments[i] == result:
            emoji = emojis[i]
            
    
    st.write(f"Your text is {result} {emoji}")
