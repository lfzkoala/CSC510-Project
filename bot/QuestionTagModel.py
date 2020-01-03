import pickle
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectKBest, chi2

class QuestionTagModel:

    def __init__(self):
        return

    # Feed question into classification model and get classified tages
    def get_Question_tags(self,question):
        with open('Ridge_classifier_model_1000_chi.sav', 'rb') as model_file:
            model = pickle.load(model_file)
        with open('Chi_transform_1000_chi.sav','rb') as chi_transform_file:
            chi_transform = pickle.load(chi_transform_file)
        vectorizer = HashingVectorizer(stop_words='english', alternate_sign=False,
                                   n_features=10000)
        vetctorized_text = vectorizer.transform([question])
        selected_text = chi_transform.transform(vetctorized_text)
        pred = model.predict(selected_text)
        tag = pred[0]
        return tag
