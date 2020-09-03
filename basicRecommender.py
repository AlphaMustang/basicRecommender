# Imports
import pandas as pd
from cleaning import openMetadata

metadata = openMetadata()
# Calculating the mean values for all ratings. 
meanValueOfAllRatings = metadata.iloc[:,22].mean()

# Calculating the number of votes which puts a film in the top 10% of votes
# cast. (Basically it's in the top 10 of people who voted for it).
votesRequiredToBeIncluded = metadata['vote_count'].quantile(0.90)

# Creating a second dataframe which only includes movies which we will 
# recommend. 
recommendingMovies = metadata.copy().loc[metadata['vote_count'] > votesRequiredToBeIncluded]

# Creating a weighted ratings with which to recommend movies with. 
def weighted_rating(x, votesRequired=votesRequiredToBeIncluded, meanRatingAcrossDataset=meanValueOfAllRatings):
    voteCount = x['vote_count']
    voteAverage = x['vote_average']
    return ( ((voteCount / (voteCount + votesRequired)) * voteAverage) + ((votesRequired / (votesRequired + voteCount)) * meanRatingAcrossDataset ) )

# Apply the weighted ratings to the recommendingMovies dataframe, storing the value
# for each row in the score column.
recommendingMovies['score'] = recommendingMovies.apply(weighted_rating, axis=1)

# Sort recommendingMovies by the highest score to the lowest score
recommendingMovies = recommendingMovies.sort_values('score', ascending=False)
# Print the top 20 films by score. 
print(recommendingMovies[['title', 'vote_count', 'vote_average', 'score']].head(20))