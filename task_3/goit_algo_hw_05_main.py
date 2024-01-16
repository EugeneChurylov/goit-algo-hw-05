import timeit

from goit_algo_hw_05_kmp import kmp_search
from goit_algo_hw_05_bm import boyer_moore_search
from goit_algo_hw_05_rk import rabin_karp_search


def measure_time(algorithm, text, pattern):
    # Вимір часу виконання алгоритму
    start_time = timeit.default_timer()
    algorithm(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Зчитування тексту з файлів (стаття 1, стаття 2)
    text1 = read_file(r"C:\Users\echur\Desktop\goit-algo-hw-05\task_3\article_1.txt")
    text2 = read_file(r"C:\Users\echur\Desktop\goit-algo-hw-05\task_3\article_2.txt")

    # Вибір підрядків для пошуку
    existing_pattern_article_1 = "відіграють важливу роль"
    existing_pattern_article_2 = "випадкових блоків займає "
    fictional_pattern_article_1 = "bluebluered"
    fictional_pattern_article_2 = "bluebluered"

    # Вимір часу для кожного алгоритму та для обох видів підрядків
    kmp_existing_time_article_1 = measure_time(kmp_search, text1, existing_pattern_article_1)
    kmp_existing_time_article_2 = measure_time(kmp_search, text2, existing_pattern_article_2)
    kmp_fictional_time_article_1 = measure_time(kmp_search, text1, fictional_pattern_article_1)
    kmp_finctional_time_article_2 = measure_time(kmp_search, text2, fictional_pattern_article_2)

    bm_existing_time_article_1 = measure_time(boyer_moore_search, text1, existing_pattern_article_1)
    bm_existing_time_article_2 = measure_time(boyer_moore_search, text1, existing_pattern_article_2)
    bm_fictional_time_article_1 = measure_time(boyer_moore_search, text2, fictional_pattern_article_1)
    bm_fictional_time_article_2 = measure_time(boyer_moore_search, text2, fictional_pattern_article_2)

    rk_existing_time_article_1 = measure_time(rabin_karp_search, text1, existing_pattern_article_1)
    rk_existing_time_article_2 = measure_time(rabin_karp_search, text1, existing_pattern_article_2)
    rk_fictional_time_article_1 = measure_time(rabin_karp_search, text2, fictional_pattern_article_1)
    rk_fictional_time_article_2 = measure_time(rabin_karp_search, text2, fictional_pattern_article_2)

    # Вивід результатів
    print(f"Кнута-Морріса-Прата для існуючого підрядка в статті 1: {kmp_existing_time_article_1} секунд")
    print(f"Кнута-Морріса-Прата для існуючого підрядка в статті 2: {kmp_existing_time_article_2} секунд")
    print(f"Кнута-Морріса-Прата для вигаданого підрядка в статті 1: {kmp_fictional_time_article_1} секунд")
    print(f"Кнута-Морріса-Прата для вигаданого підрядка в статті 2: {kmp_finctional_time_article_2} секунд")

    print(f"Боєра-Мура для існуючого підрядка в статті 1: {bm_existing_time_article_1} секунд")
    print(f"Боєра-Мура для існуючого підрядка в статті 2: {bm_existing_time_article_2} секунд")
    print(f"Боєра-Мура для вигаданого підрядка в статті 1: {bm_fictional_time_article_1} секунд")
    print(f"Боєра-Мура для вигаданого підрядка в статті 2: {bm_fictional_time_article_2} секунд")

    print(f"Рабіна-Карпа для існуючого підрядка в статті 1: {rk_existing_time_article_1} секунд")
    print(f"Рабіна-Карпа для існуючого підрядка в статті 2: {rk_existing_time_article_2} секунд")
    print(f"Рабіна-Карпа для вигаданого підрядка в статті 1: {rk_fictional_time_article_1} секунд")
    print(f"Рабіна-Карпа для вигаданого підрядка в статті 2: {rk_fictional_time_article_2} секунд")

    
    print(f"{'| Algorithm': <20} | {'Existing pattern': <20} | {'Fictional pattern': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")

    print(" Стаття 1")
    print(f"{'| KMP': <20} | {kmp_existing_time_article_1:<20.7f} | {kmp_fictional_time_article_1:<20.7f}")
    print(f"{'| BM': <20} | {bm_existing_time_article_1:<20.7f} | {bm_fictional_time_article_1:<20.7f}")
    print(f"{'| RK': <20} | {rk_existing_time_article_1:<20.7f} | {rk_fictional_time_article_1:<20.7f}")

    print(" Стаття 2")
    print(f"{'| KMP': <20} | {kmp_existing_time_article_2:<20.7f} | {kmp_finctional_time_article_2:<20.7f}")
    print(f"{'| BM': <20} | {bm_existing_time_article_2:<20.7f} | {bm_fictional_time_article_2:<20.7f}")
    print(f"{'| RK': <20} | {rk_existing_time_article_2:<20.7f} | {rk_fictional_time_article_2:<20.7f}")

    