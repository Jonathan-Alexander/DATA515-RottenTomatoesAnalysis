from rotten_tomatoes.utils.data_cleaning import (
    CriticsDataCleaner,
    MoviesDataCleaner,
    BestPictureOscarsDataCleaner,
    AnyWinOscarsDataCleaner,
    MergeExpansionException,
)

any_win_data = AnyWinOscarsDataCleaner().run()
best_picture_data = BestPictureOscarsDataCleaner().run()

movies_data = MoviesDataCleaner().run()
critics_data = CriticsDataCleaner().run()

# First, merge the two Rotten Tomatoes datasets together.
# Merge just the movie title from movies data onto critics data.
# We are only using the critic scores at this time, but this may change.
movie_titles = movies_data[["rotten_tomatoes_link", "movie_title"]].drop_duplicates()
start_rows = critics_data.shape[0]
# Do an inner merge, to drop movies we don't have titles for
critics_data = critics_data.merge(movie_titles, on="rotten_tomatoes_link", how="inner")
end_rows = critics_data.shape[0]
if end_rows > start_rows:
    raise Exception(
        "Number of rows increased after merging with movie title. This is unexpected."
    )
if end_rows < start_rows:
    print(
        f"{start_rows - end_rows} rows have been dropped "
        "because they did not match with a movie title."
    )

# At this point, data should be uniquely identified by critic name and rotten tomatoes link.

# Merge the oscars data onto rotten tomatoes on movie title.
# The Oscars time series goes back much farther than Rotten Tomatoes (1928 vs 1998),
# and some movie titles are different.
best_picture_data.rename(columns={"film": "movie_title"}, inplace=True)
any_win_data.rename(columns={"film": "movie_title"}, inplace=True)

# Do an inner merge, to drop movies we don't have scores for
# We will expect this to expand the rows, because there is more than 1 critic review per movie
best_picture_data = best_picture_data.merge(critics_data, on="movie_title", how="inner")
best_picture_data = best_picture_data.drop_duplicates()

print(f"Writing best picture data...")
best_picture_data.to_csv("./data/best_picture_data.csv")


# Do an inner merge, to drop movies we don't have scores for
any_win_data = any_win_data.merge(critics_data, on="movie_title", how="inner")
any_win_data = any_win_data.drop_duplicates()

print(f"Writing any win data...")
any_win_data.to_csv("./data/any_win_data.csv")
