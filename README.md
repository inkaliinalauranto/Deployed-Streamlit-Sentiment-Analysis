# Moduuli 3, bonustehtävä - Cloud-based Streamlit Frontend Deployment

Tässä tehtävässä on Streamlit-sovelluskehyksen avulla toteutettu yksinkertainen sovellus, joka on otettu käyttöön ja [julkaistu](https://deployed-sentiment-analysis.streamlit.app/) Streamlitin Community Cloud -pilvipalvelun kautta. Sovelluksessa hyödynnetään moduulissa 2 tehtyä tunneanalyysimallia, jonka avulla käyttäjän syötteestä analysoidaan syötteen tunnelma. Analysoitu tunnelma tuodaan käyttöliittymään Streamlitin toimintojen avulla:

![user interface](images/ui.png)

## Projektin kloonaaminen ja konfigurointi paikallisesti

```
git clone https://github.com/inkaliinalauranto/Deployed-Streamlit-Sentiment-Analysis.git  
```

```
cd Deployed-Streamlit-Sentiment-Analysis
```
```
python -m venv .venv
```
```
.venv\Scripts\activate.bat
```
```
python -m pip install -r requirements.txt
```
```
streamlit run app.py
```

