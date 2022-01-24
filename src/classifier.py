import sklearn
import joblib
import __main__
from src.transformations import *
from sklearn.ensemble import GradientBoostingClassifier


__main__. translate = translate
__main__. strip_punctuations = strip_punctuations
__main__. remove_stopwords = remove_stopwords
__main__. transform_text = transform_text

class Classifier:
    def __init__(self, path):
        self.model = joblib.load(path)

    async def get_prediction(self, doc):
        classes = self.model.classes_.tolist()
        y_pred_class = self.model.predict([doc])[0]
        y_pred = self.model.predict_proba([doc])[0][classes.index(y_pred_class)]
        
        return y_pred_class, y_pred