from sklearn import svm
import pandas as pd


class SupportVectorMachine:

    def __init__(self, array_labelgood, array_labelbad):
        # fit the model
        classification = svm.SVC(cache_size=700)
        classification.fit(array_labelgood, array_labelbad)

        # get support vectors
        classification.support_vectors_
        # get indices of support vectors
        classification.support_
        # get number of support vectors for each class
        classification._n_support_
