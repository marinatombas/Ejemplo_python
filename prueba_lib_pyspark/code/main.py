import read_prepare_save
import most_popular
import config
import best_film

#separate df titles and person
titles_dfs=read_prepare_save.filter_dfs(config.dfs,'title')
credits_dfs=read_prepare_save.filter_dfs(config.dfs, 'person_id')

def most_popular_actor_director():
    """
    Uses functions to calculate the 5 most common actors and 5 most
    common directors and prints it and also saves it in new df popular_actors and
    popular_directors
    :return:
    """
    # CALCULATE ACTOR AND DIRECTOR IN MOST FILMS
    # concat dfs
    concat_credits = read_prepare_save.concat_df(credits_dfs)
    # clean df:
    clean_credits = most_popular.clean_credits(concat_credits)
    #print(clean_df)
    # separate actors and directors in diferent df
    actors_df = read_prepare_save.select_values_from_column(clean_credits,'role','ACTOR')
    directors_df = read_prepare_save.select_values_from_column(clean_credits,'role','DIRECTOR')

    # creates a new df and shows the top 5 actors
    popular_actors = most_popular.id_count(actors_df)
    print(f'These are the 5 most popular actors {popular_actors.head(5)}')

    # prints the top 5 directors
    popular_directors = most_popular.id_count(directors_df)
    print(f'These are the 5 most popular directors {popular_directors.head(5)}')

    # save df
    read_prepare_save.save_df_csv(popular_actors, "popular_actors")
    read_prepare_save.save_df_csv(popular_directors, "popular_directors")

def award_best_film():
    #concat df
    concat_films=read_prepare_save.concat_df(titles_dfs)

    #clean df
    clean_films=best_film.clean_df(concat_films)

    #select movies
    movies_df= read_prepare_save.select_values_from_column(clean_films, 'type','MOVIE')

    #Rank movies
    ranked_films=best_film.rank(movies_df)
    ranked_films_directors=best_film.join(ranked_films)

    #Top 5 movies
    best_movies= ranked_films_directors.sort_values(by='score', ascending=False)
    print(f'These are the best ranked movies\n{best_movies.head(5)}')
    read_prepare_save.save_df_csv(best_movies, "best_movies")


def main():
   #most_popular_actor_director()
   award_best_film()

if __name__ == "__main__":
    main()






