from utils import CriticsDataCleaner, MoviesDataCleaner, OscarsDataCleaner

critics_data = CriticsDataCleaner().run()
movies_data = MoviesDataCleaner().run()
oscars_data = OscarsDataCleaner().run()

# Merge the rotten tomatoes link. 
# Because these datasets are coming from the same sources, 
# assume that these IDs are cleaned and unique. 
# Assume that  
full_data = critics_data.merge(movies_data, on='rotten_tomatoes_link', how='inner')
full_data = full_data.reset_index(drop=True)

# Merge the oscars data onto rotten tomatoes on movie title. 
# The Oscars time series goes back much farther than Rotten Tomatoes (1928 vs 1998),
# so do a left merge here. 
# Do some cleaning here to make sure the names are not specified differently. 
oscars_data.rename(columns={'film': 'movie_title'}, inplace=True)
test = full_data.merge(oscars_data, on = 'movie_title', how='left')

print(f"Movies found in Oscars dataset, but not Rotten Tomatoes. Review by hand.")
test.loc[test['category'].isna(), 'movie_title'].unique()

# There are 14k observations here - too many to review by hand. 
# Simply do an inner merge and note this as a limitation to the modeling. 
full_data = full_data.merge(oscars_data, on = 'movie_title', how='inner')
full_data.to_csv('./data/full_data.csv')