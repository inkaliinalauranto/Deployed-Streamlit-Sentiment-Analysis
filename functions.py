import time

# Alla olevissa funktiossa luodaan sisältöä HTML-koodipohjaisesti. Nämä 
# ratkaisut on tehty seuraavia esimerkkejä mukaillen:
#
# Kekre, S. 2021: 
# https://discuss.streamlit.io/t/passing-variable-containing-text-to-markdown/16069/2
# 
# y2ntfk8e 2023:
# https://discuss.streamlit.io/t/create-animation-for-messages-when-button-is-clicked/39610


# Funktio palauttaa HTML-koodia merkkijonomuodossa. HTML-koodi palauttaa 
# divin, joka pitää sisällään parametrina välitetyn tekstin. Merkkijono 
# sisältää myös tyyliluokan määrittelyn tätä diviä varten. 
def html_title(text: str) -> str:
    html_title_str = (f"""
    <style>
    .title {{
        font-size: 1.17em; 
        font-weight: bold; 
        margin-bottom: 1em; 
    }}
    </style>
    <div className=title>{text}</div>
    """)
    
    return html_title_str


# Funktio palauttaa HTML-koodia merkkijonomuodossa. Merkkijonon HTML-koodi
# palauttaa div-elementin, jossa on sekä staattista tekstiä että parametrina 
# saatu dynaaminen sana ja emoji. Merkkijono sisältää myös tyyliluokan, joka
# asetetaan divin luokaksi. Sen avulla diville saadaan animaatio. Tyyliluokka 
# nimetään dynaamisesti hyödyntämällä aikaleimaa, jotta elementti renderöidään 
# aina uudestaan, kun käyttäjäsyöte lähetetään. Tämän aikaleimaa hyödyntävän 
# dynaamisen nimeämisen logiikan muodostamisessa käytin apuna ChatGPT:tä.
def html_result(result: str, emoji: str) -> str:
    # time-kirjaston time-metodi palauttaa ajonaikaisen UCT-ajan sekunteina.
    # (Lähde: https://www.tutorialspoint.com/python/time_time.htm.)
    # Koska tätä leimaa käytetään CSS-luokan nimeämisessä, muutetaan se 
    # ensin liukuluvusta merkkijonoksi. Sen jälkeen erotellaan leima kahteen 
    # osaan pisteen kohdalta, koska kyseessä oli alunperin liukuluku. 
    # Yhdistetään lopuksi erotellut osat P-merkillä. Näin vältytään siltä, 
    # ettei CSS-luokan nimeen tule vääränlaista merkkiä (.), mutta luokan nimi 
    # säilyy edelleen ainutkertaisena.
    unique_id = "P".join(str(time.time()).split("."))

    # Animaation tuottava CSS-luokka on tehty seuraavan esimerkin mukaan:
    # https://dev.to/tiaeastwood/super-simple-css-animation-for-fade-in-on-page-load-2p8m
    html_result_str = (f"""
    <style>
    @keyframes fadeInUp-{unique_id} {{
        0% {{
            transform: translateY(100%);
            opacity: 0;
        }}
        100% {{
            transform: translateY(0%);
            opacity: 1;
        }}
    }}

    .fadeInUp-animation-{unique_id} {{
        animation: 1.5s fadeInUp-{unique_id};
        font-size: 1.5em;
        margin-top: 0.5em;
    }}
    </style>
    
    <div className="fadeInUp-animation-{unique_id}">Your text is <b>{result}</b> {emoji}</div>
    """)

    return html_result_str