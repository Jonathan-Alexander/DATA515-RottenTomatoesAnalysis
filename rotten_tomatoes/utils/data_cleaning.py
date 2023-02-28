"""Helper classes for raw data cleaning."""
from typing import Optional
import pandas as pd

# pylint: disable=R0903,C0103


class ValidationException(Exception):
    """Raised for data validation errors."""

class MergeExpansionException(Exception):
    """Raised when a merge unexpectedly increases rows."""


class DataCleaner:
    """Base class. Defines interface for data cleaning."""

    keep_columns = None

    def __init__(self):
        pass

    def run(self) -> pd.DataFrame():
        """Runs all data loading and cleaning steps."""
        data = self._read()
        data = self._clean(data)
        self._validate(data)

        return data

    def _read(self) -> pd.DataFrame:
        raise NotImplementedError()

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError()

    def _validate(self, data: pd.DataFrame) -> None:
        for col in self.keep_columns:
            if col not in data:
                raise ValidationException(f"Missing {col} from data!")

    def _validate_rating_col(self, data: pd.DataFrame, col: str) -> None:
        if col not in data.columns:
            raise ValidationException(f"Column {col} not available in passed data!")
        if data.loc[data[col].isna()].shape[0] > 0:
            raise ValidationException(f"Null values not allowed in {col}!")
        if not all(isinstance(x, float) for x in data[col]):
            raise ValidationException(f"Found non-float values for {col}!")


class CriticsDataCleaner(DataCleaner):
    """Clean critics dataset."""

    keep_columns = [
        "rotten_tomatoes_link",
        "critic_name",
        "top_critic",
        "review_type",
        "review_score",
    ]

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv("./data/rotten_tomatoes_critic_reviews.csv")
        return data[self.keep_columns]

    def _validate_single_score(self, score: float, original_score: str) -> float:
        """If score > 100, cap at 100."""
        if score > 100:
            print(
                f"Score greater than 100! Current score is {score}, ",
                f"original score was {original_score}. Correcting to 100.",
            )
            return 100.0
        return score

    def _clean_single_score(self, score: str) -> Optional[float]:
        """Cleans a single score to a 0-100 scale."""
        original_score = score  # For logging

        # Correct a few scores manually.
        manual_corrections = {
            "35/4": 87.5,  # Assuming 3.5/4
            "67/10": 67.0,
            "87/10": 87.0,
            "920": 92.0,
            "76/10": 76.0,
            "75/10": 75.0,
            "910": 91.0,
            "25/4": 62.5,  # Assuming 2.5/4
            "45/5": 90.0,
            "73/10": 73.0,
        }
        if score in manual_corrections:
            return manual_corrections[score]
        substitutions = {
            "A+": 98,
            "A": 95,
            "A-": 93,
            "B+": 88,
            "B": 85,
            "B-": 83,
            "C+": 78,
            "C": 75,
            "C-": 73,
            "D+": 68,
            "D": 65,
            "D-": 63,
            "E": 50,
            "F": 40,
        }
        # If score can already be converted to float, return.
        try:
            return self._validate_single_score(float(score), original_score)
        except:  # pylint: disable=W0702
            pass
        # Then, clean.
        # First, take any observations with a "/" and divide them.
        if "/" in score:
            numerator, denominator = score.split("/")
            numerator = float(numerator)
            denominator = float(denominator)
            if denominator == 0:
                return None
            score = (float(numerator) / float(denominator)) * 100
            return self._validate_single_score(score, original_score)

        # Handle alphanumeric case. Remove any spaces,
        # and then use dictionary.
        score = score.replace(" ", "")
        if score not in substitutions:
            raise ValueError(f"Unable to process score {score}.")
        return substitutions[score]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        1.) Subset to the columns we care about
        2.) Because we only care about the numerical rating, drop any observations where
            rating is null.
        3.) Standardize review scores.
        """
        data = data.loc[~data["review_score"].isna()]

        # Standardize review scores between 0-100.
        # There are both numerical, ratio, and letter scores.
        cleaned_review_scores = []
        for _, row in data.iterrows():
            cleaned_review_scores.append(self._clean_single_score(row["review_score"]))

        data["review_score"] = cleaned_review_scores

        # Drop out any NA values from review score
        return data.loc[~data["review_score"].isna()]

    def _validate(self, data: pd.DataFrame) -> None:
        """
        1.) Assert no null values in reviews
        2.) Assert the 'keep_columns' are in the data
        """
        super()._validate(data)
        self._validate_rating_col(data, "review_score")


class MoviesDataCleaner(DataCleaner):
    """Clean movies dataset."""

    keep_columns = [
        "rotten_tomatoes_link",
        "movie_title",
        "tomatometer_rating",
        "audience_rating",
    ]

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv("./data/rotten_tomatoes_movies.csv")
        return data[self.keep_columns]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        """Clean data."""
        data = data.loc[~data["tomatometer_rating"].isna()]
        data = data.loc[~data["audience_rating"].isna()]
        return data

    def _validate(self, data: pd.DataFrame) -> None:
        """
        1.) Assert no null values in tomatometer or audience rating
        2.) Assert all rating columns between 0-100
        """
        super()._validate(data)
        self._validate_rating_col(data, "tomatometer_rating")
        self._validate_rating_col(data, "audience_rating")


class OscarsDataCleaner(DataCleaner):
    """Clean Oscars dataset."""

    keep_columns = ["year_film", "category", "film", "winner"]

    def _read(self) -> pd.DataFrame:
        data = pd.read_csv("./data/the_oscar_award.csv")
        return data[self.keep_columns]

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        # Drop any NaNs in winner column
        data = data.loc[~data["winner"].isna()]
        return data


class BestPictureOscarsDataCleaner(OscarsDataCleaner):
    """Produce a dataset of best-picture winners."""

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        data = super()._clean(data)
        # Only keep best-picture winning categories
        best_picture_categories = [
            "BEST MOTION PICTURE",
            "BEST PICTURE",
            "OUTSTANDING PICTURE",
            "OUTSTANDING MOTION PICTURE",
            "Best Picture",
            "BEST MOTION PICTURE",
        ]
        data = data.loc[data["category"].isin(best_picture_categories)]
        data = data.drop_duplicates().reset_index(drop=True)
        return data

    def _validate(self, data: pd.DataFrame) -> None:
        super()._validate(data)
        # Assert no duplicate years of winners
        winner_years = data.loc[data["winner"] is True, "year_film"]
        value_counts = winner_years.value_counts().reset_index()
        if value_counts.loc[value_counts["year_film"] > 1].shape[0] > 0:
            raise ValidationException(
                "More than one best picture winner found in a given year!"
            )
        if data.loc[data["winner"].isna()].shape[0] > 0:
            raise ValidationException("NAs found in winner categories! Review.")


class AnyWinOscarsDataCleaner(OscarsDataCleaner):
    """Calculates movies with any win from Oscars dataset."""

    def _clean(self, data: pd.DataFrame) -> pd.DataFrame:
        data = super()._clean(data)
        data["winner"] = data["winner"].astype("int")
        data = data.groupby(["year_film", "film"]).sum("winner").reset_index()
        data.columns = ["year_film", "film", "num_wins"]
        return data

    def _validate(self, data: pd.DataFrame) -> None:
        pass
