import streamlit as st
from nlp import text_clf
from functions import html_result, html_title

# Haetaan markdown-tyyppiä olevan elementin sisällöksi merkkijonomuotoinen 
# HTML-otsikko-div. Kun unsafe_allow_html-parametrin asettaa arvoon True, 
# käsitellään HTML-tageja raakatekstin sijaan HTML-lausekkeina.
# Lähde: https://docs.streamlit.io/develop/api-reference/text/st.markdown
st.markdown(html_title("What are you currently thinking?"), unsafe_allow_html=True)

# Syötekenttänä käytetään Streamlitin omaa text_input-komponenttia: 
# Lähde: https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
user_input = st.text_input(label="What are you currently thinking?",
                           label_visibility="collapsed",
                           placeholder="Write a word or a sentence here")

# Kun käyttäjä syöttää tekstin enteriä painamalla, siirrytään if-lauseen 
# sisään: 
if user_input:
    # Ennustetaan käyttäjän syötteen tunne text_clf-muuttujassa olevan 
    # koulutusmallin predict-metodia hyödyntämällä. Metodi palauttaa tuloksen 
    # arrayna, jossa tässä tapauksessa on vain yksi alkio:
    result = text_clf.predict([user_input])[0]
    # Koska tulostekstin sisältö luodaan HTML-koodilla, käytetään UTF-8 
    # Emoji Faces -hymiöitä. Haluttujen hymiöiden HTML-viittaukset hain 
    # seuraavasta lähteestä: 
    # https://www.w3schools.com/charsets/ref_emoji_smileys.asp
    emoji = "&#128528;"

    sentiments = ["positive", "neutral", "negative"]
    emojis = ["&#128522;", "&#128528;", "&#128530;"]

    # Käydään sentiments-listan jokainen alkio läpi. Jos käyttäjäsyötteestä 
    # ennustettu tunne vastaa jotakin listan alkiota, haetaan 
    # emoji-muuttujaan emojis-listasta alkio samalla indeksillä. emojis-lista 
    # on järjestelty siten, että kussakin indeksissä oleva hymiö vastaa 
    # sentiment-listan samassa indeksissä olevan sanan merkitystä.
    for i in range(0, len(sentiments)):
        if sentiments[i] == result:
            emoji = emojis[i]
            break

    # Tuodaan käyttöliittymään tulos, jossa käyttäjälle näytetään, mikä 
    # oli analyysin perusteella käyttäjän syötteen vallitseva tunne: 
    st.markdown(html_result(result, emoji), unsafe_allow_html=True)
