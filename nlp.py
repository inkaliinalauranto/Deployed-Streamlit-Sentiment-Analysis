import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

train_df = pd.read_csv("./train.csv", encoding="ISO-8859-1")
test_df = pd.read_csv("./test.csv", encoding="ISO-8859-1")

train_df.dropna(inplace=True)
test_df.dropna(inplace=True)

x_train = train_df["text"]
y_train = train_df["sentiment"]

x_test = test_df["text"]
y_test = test_df["sentiment"]


text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC())])

text_clf.fit(x_train, y_train)

