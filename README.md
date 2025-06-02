# prueba_lib_pyspark

# Movie Analysis: Extraction of Most Active Actors and Directors, and Top-Rated Movies

This Python project analyzes movie data from multiple CSV files containing information about movie credits (actors, directors, etc.) and movies with their IMDb and TMDb scores. The project performs the following tasks:

1. **Extraction of Actors and Directors**:
   - Identifies the actors who appear in the most movies.
   - Identifies the directors who have directed the most movies.
   - Displays the top 5 most active actors and directors.

2. **Calculation of Top-Rated Movies**:
   - Calculates an average score for each movie using IMDb and TMDb ratings.
   - Sorts movies based on the average score.
   - Displays the top 5 highest-rated movies with their director.

3. **Storage and Visualization**:
   - Saves the analysis results in multiple DataFrames:
     - One for the most active actors.
     - One for the most active directors.
     - Another for the top-rated movies.

## Files
- `credits.csv`: Contains the credits (actors, directors, etc.) for each movie and show.
- `credits2.csv`: Complementary or updated version of `credits.csv`, with additional or modified information.
- `titles.csv`: Contains the titles and ratings for each film.
