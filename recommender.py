# Imports
import pandas as pd

metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

print(metadata.head(5))