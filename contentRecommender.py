# imports
import pandas as pd
from cleaning import openMetadata
from sklearn.feature_extraction.text import TfidfVectorizer

# Open the metadata dataframe which has been cleaned to remove any 
# film with 0 user votes as they are deemed useless.
metadata = openMetadata()

# Drop rows with NaN values in their overview to save space. 
metadata.dropna(axis=0, how="any", subset=['overview'], inplace=True)

# Set up the vectorizer with English stop words. 
tfidf = TfidfVectorizer(stop_words='english')

# Construct the required TF-IDF matrix by fitting and transforming
# the data.
tfidfMatrix = tfidf.fit_transform(metadata['overview'])

#from sklearn.metrics.pairwise import linear_kernel
# Compute the cosine similarity matrix
#cosineSim = linear_kernel(tfidfMatrix.copy(), tfidfMatrix.copy())
