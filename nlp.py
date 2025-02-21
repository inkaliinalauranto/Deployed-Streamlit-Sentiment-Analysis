import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Luetaan koulutusaineisto omaan muuttujaansa:
train_df = pd.read_csv("./data_material/train.csv", encoding="ISO-8859-1")

# Poistetaan tietueet, joissa on "tyhjiä arvoja":
train_df.dropna(inplace=True)

# Erotellaan text- ja sentiment-sarakkeiden arvot omiin muuttujiinsa: 
x_train = train_df["text"]
y_train = train_df["sentiment"]

# Luodaan koulutusmalli: 
text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC())])

text_clf.fit(x_train, y_train)

