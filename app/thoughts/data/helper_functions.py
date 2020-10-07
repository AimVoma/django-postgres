class TFTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, min_df=1, ngram_range=(1,1), norm=None, max_features=None):
        self.vectorizer = None

        args, _, _, values = inspect.getargvalues(inspect.currentframe())
        values.pop("self")

        for arg, val in values.items():
            setattr(self, arg, val)

    def transform(self, sentences, y=None):
        return self.vectorizer.transform(sentences)

    def fit(self, corpus, y=None):
        self.vectorizer = TfidfVectorizer(token_pattern=r'\w{2,}',
                                          sublinear_tf=True,
                                          analyzer='word',
                                          ngram_range=self.ngram_range,
                                          min_df=self.min_df,
                                          max_features = self.max_features,
                                          norm=self.norm)
        self.vectorizer.fit(corpus)
        return self

    def fit_transform(self, corpus, y=None):
        self.vectorizer = TfidfVectorizer(token_pattern=r'\w{2,}',
                                          sublinear_tf=True,
                                          analyzer='word',
                                          ngram_range=self.ngram_range,
                                          min_df=self.min_df,
                                          norm=self.norm)
        self.vectorizer.fit(corpus)
        return self.transform(corpus)

    def get_feature_names(self):
        try:
            return self.vectorizer.get_feature_names()
        except:
            return False
