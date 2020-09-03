# Imports
import pandas as pd

# Importing the metadata file from the CSV
metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

# Removing data
metadata = metadata[metadata.vote_count != 0]

meanValueOfAllRatings = metadata.iloc[:,22].mean()
print(meanValueOfAllRatings)