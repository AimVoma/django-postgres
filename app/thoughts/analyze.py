# import bcrypt
# import random
# import logging
# import inspect
# import dill as pickle
#
# from sklearn.datasets import load_files
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import GridSearchCV
# from sklearn.pipeline import Pipeline
# from sklearn.svm import LinearSVC
# from sklearn.base import BaseEstimator, TransformerMixin
#
# import os, sys
# import joblib
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# data_fpath = os.path.join(BASE_DIR, 'thoughts/data/')
#
# class TFTransformer(BaseEstimator, TransformerMixin):
#
#     def __init__(self, min_df=1, ngram_range=(1,1), norm=None, max_features=None):
#         self.vectorizer = None
#
#         args, _, _, values = inspect.getargvalues(inspect.currentframe())
#         values.pop("self")
#
#         for arg, val in values.items():
#             setattr(self, arg, val)
#
#     def transform(self, sentences, y=None):
#         return self.vectorizer.transform(sentences)
#
#     def fit(self, corpus, y=None):
#         self.vectorizer = TfidfVectorizer(token_pattern=r'\w{2,}',
#                                           sublinear_tf=True,
#                                           analyzer='word',
#                                           ngram_range=self.ngram_range,
#                                           min_df=self.min_df,
#                                           max_features = self.max_features,
#                                           norm=self.norm)
#         self.vectorizer.fit(corpus)
#         return self
#
#     def fit_transform(self, corpus, y=None):
#         self.vectorizer = TfidfVectorizer(token_pattern=r'\w{2,}',
#                                           sublinear_tf=True,
#                                           analyzer='word',
#                                           ngram_range=self.ngram_range,
#                                           min_df=self.min_df,
#                                           norm=self.norm)
#         self.vectorizer.fit(corpus)
#         return self.transform(corpus)
#
#     def get_feature_names(self):
#         try:
#             return self.vectorizer.get_feature_names()
#         except:
#             return False
#
# if not os.path.exists(os.path.join(BASE_DIR, data_fpath, 'txt_sentoken')):
#     os.system('wget http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz -P {}'.format(data_fpath))
#     os.system('tar xzf {}/review_polarity.tar.gz -C {}'.format(data_fpath, data_fpath))
#     os.system('rm -rf {}/review_polarity.tar.gz'.format(data_fpath))
# else:
#     pass
#
# # Get an instance of a logger
# logger = logging.getLogger(__name__)
#
#
#
# class SVMAnalyzer:
#     '''
#     List the user's thoughts
#     '''
#     def __init__(self):
#         self.data = load_files(os.path.join(data_fpath, 'txt_sentoken'))
#         self.hyperParam = {"tfidf__ngram_range": [(1, 1), (1, 2), (1, 3)], "svc__C": [.01, .1, 1]}
#         self.model = None
#
#     def runModel(self):
#         # print(len(self.data.data))
#         # sys.exit(0)
#         # print(type(self.data))
#
#         clf = Pipeline([("tfidf", TFTransformer()), ("svc", LinearSVC())])
#
#         GridSearch = GridSearchCV(clf, self.hyperParam, verbose=2, n_jobs=-1)
#         GridSearch.fit(self.data.data, self.data.target)
#         print('----- Printing Best Score & Estimator')
#         print('Best Hyper-Parameters: {}'.format(GridSearch.best_estimator_))
#         print('Best Raw Acc Score: {}'.format(GridSearch.best_score_))
#         print('Saving Pipeline TFIDF - SVM')
#         self.model = GridSearch.best_estimator_
#
#         return self
#
#     def saveModel(self):
#         if not self.model:
#             logger.error('ML model is empty')
#         else:
#             print('----- Saving SVM model')
#             # joblib.dump(self.model, os.path.join(data_fpath, 'SentimentSVM.pkl'), compress = 1)
#             with open(os.path.join(data_fpath, 'SentimentSVM.pkl'), 'wb') as file:
#                 pickle.dump(self.model, file)
#
# SVMAnalyzer().runModel().saveModel()