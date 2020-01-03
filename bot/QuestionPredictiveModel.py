import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import SGDClassifier, RidgeClassifier
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
import pickle

def convert_text_feature(option, X_train, X_test):
    vectorizer = None
    if option == 'use_hashing':
        vectorizer = HashingVectorizer(stop_words='english', alternate_sign=False,
                                       n_features=10000)
        X_training = vectorizer.transform(X_train.astype('U'))
        X_testing = vectorizer.transform(X_test.astype('U'))
        return X_training, X_testing, vectorizer
    if option == 'use_tfidf':
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                     stop_words='english')
        X_training = vectorizer.fit_transform(X_train.astype('U'))
        X_testing = vectorizer.fit_transform(X_test.astype('U'))
        return X_training, X_testing, vectorizer

if __name__ == '__main__':
    total = pd.read_csv('/Users/zwu/CSC510/QuestionModel/data_20.csv', encoding='latin-1')
    X_train, X_test, y_train, y_test = train_test_split(total['Text'], total['Tag'], random_state=42, test_size=0.2,
                                                        shuffle=True)
    X_train_1, X_test_1, vectorizer = convert_text_feature('use_hashing', X_train, X_test)
    ch2 = SelectKBest(chi2,1000)
    X_train_1 = ch2.fit_transform(X_train_1, y_train)
    X_test_1 = ch2.transform(X_test_1)
    # filename1='/Users/zwu/CSC510/QuestionModel/Chi_transform_1000_chi.sav'
    # pickle.dump(ch2, open(filename1, 'wb'))
    model = RidgeClassifier(tol=1e-2, solver="lsqr",fit_intercept=False)
    # model = SGDClassifier(alpha=.0001, n_iter_no_change=50,
    #                                    penalty="elasticnet")
    model.fit(X_train_1, y_train)
    filename3 = '/Users/zwu/CSC510/QuestionModel/SGDClassifier_model_1000_chi.sav'
    pickle.dump(model, open(filename3, 'wb'))
    predicted = model.predict(X_test_1)
    score = metrics.accuracy_score(y_test, predicted)
    print(predicted)
    print(score)
#    print(predicted)

 #   target_names = total['Tag'].unique()
 #   print(target_names)



'''Get top 20 tags'''
# tagCount = collections.Counter(list(total['Tag'])).most_common(20)
#
# tagList = []
# for ele in tagCount:
#     tagList.append(ele[0])
#
# data_with_20_tags = total.loc[total['Tag'].isin(tagList)]
#
# data_with_20_tags.to_csv('/Users/zwu/CSC510/QuestionModel/data_20.csv', index=False)



'''Preprocess body'''
# global EMPTY
# EMPTY = ''
#
#
# def clean_text(text):
#     global EMPTY
#     EMPTY = ''
#
#     if not isinstance(text, str):
#         return text
#     text = re.sub('<pre><code>.*?</code></pre>', EMPTY, text)
#
#     def replace_link(match):
#         return EMPTY if re.match('[a-z]+://', match.group(1)) else match.group(1)
#
#     text = re.sub('<a[^>]+>(.*)</a>', replace_link, text)
#     return re.sub('<[^>]+>', EMPTY, text)
#
#
# total['Text'] = total['Body'].apply(clean_text).str.lower()
# #print(total['Text'][0])
# total.Text = total.Text.apply(lambda x: x.replace('"','').replace("\n","").replace("\t",""))
#
#total.to_csv('/Users/zwu/CSC510/QuestionModel/precessed_total.csv', columns=['Title','Text','Tag'], index=False)