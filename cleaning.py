import pandas as pd

def openMetadata():
    # Importing the metadata file from the CSV
    metadata = pd.read_csv('movies_metadata.csv', low_memory=False)
    # Removing data for films which had 0 user votes as it is useless for us. 
    metadata = metadata[metadata.vote_count != 0]
    return metadata