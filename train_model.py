import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


class TrainModel:
    def __init__(self, category):
        self.cv = CountVectorizer(max_features=5000)
        self.category = category
        self.classifier = None

    def train(self, x, y):
        x_train = self.cv.fit_transform(x).toarray()
        y_train = np.array(y)
        self.classifier = RandomForestClassifier(
            n_estimators=100, criterion="entropy", random_state=0
        ).fit(x_train, y_train)
        return self

    def predict(self, x_test):
        y_pred = self.classifier.predict(self.cv.transform(x_test))
        categs = [self.category.query(f"categoryId == {y}").iloc[0, 1] for y in y_pred]
        return pd.DataFrame(data={"venue": x_test, "category": categs}).reset_index(
            drop=True
        )
