from prueba_lib_pyspark.code.film_analysis import FilmAnalysis
from config import BASE_PATH


def main():
    top_n = 10
    film_analysis_obj = FilmAnalysis(BASE_PATH)
    film_analysis_obj.most_popular_actor_director(top_n)
    film_analysis_obj.award_best_film()


if __name__ == "__main__":
    main()
