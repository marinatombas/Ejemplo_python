import pandas_utils
import most_popular
from config import DataReader, base_path
import best_film

# separate df titles and person
# titles_dfs = pandas_utils.filter_dfs(config.dfs, 'title')
# credits_dfs = pandas_utils.filter_dfs(config.dfs, 'person_id')


def most_popular_actor_director():
    """
    Uses functions to calculate the 5 most common actors and 5 most
    common directors and prints it and also saves it in new df popular_actors and
    popular_directors
    :return:
    """
    dr = DataReader(base_path)
    dr.read_all_files()
    credits_df = dr.table_dict["credits.csv"]
    credits_df2 = dr.table_dict["credits2.csv"]
    credits_dfs = [credits_df.df, credits_df2.df]
    # CALCULATE ACTOR AND DIRECTOR IN MOST FILMS
    # concat dfs
    concat_credits = pandas_utils.concat_df(credits_dfs)
    # clean df:
    clean_credits = most_popular.clean_credits(concat_credits)

    # separate actors and directors in diferent df
    actors_df = pandas_utils.select_values_from_column(clean_credits, 'role', 'ACTOR')
    directors_df = pandas_utils.select_values_from_column(clean_credits, 'role', 'DIRECTOR')

    # process and save
    most_popular.process_and_save(actors_df, 'actors')
    most_popular.process_and_save(directors_df, 'directors')


def award_best_film():
    # concat df
    dr = DataReader(base_path)
    dr.read_all_files()
    titles_1=dr.table_dict["titles.csv"]
    titles_dfs=[titles_1.df]
    concat_films = pandas_utils.concat_df(titles_dfs)

    # clean df
    clean_films = best_film.clean_df(concat_films)

    # select movies
    movies_df = pandas_utils.select_values_from_column(clean_films, 'type', 'MOVIE')

    # Rank movies
    ranked_films = best_film.rank(movies_df)
    ranked_films_directors = best_film.join(ranked_films)

    # Top 5 movies
    best_movies = ranked_films_directors.sort_values(by='score', ascending=False)
    print(f'These are the best ranked movies\n{best_movies.head(5)}')
    pandas_utils.save_df_csv(best_movies, "best_movies")


def main():
    most_popular_actor_director()
    award_best_film()


if __name__ == "__main__":
    main()
