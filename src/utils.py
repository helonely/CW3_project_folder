

def get_filtered_list(list_vacancies: list, filter_words: list):
    # Фильтруем вакансии по ключевым словам
    filtered_vacancies = [vacancy for vacancy in list_vacancies if
                          vacancy.snippet_req and  # Проверяем, что snippet_req не является None
                          any(word.lower() in vacancy.snippet_req.lower() for word in filter_words)]
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list, min_salary: int):
    # Фильтруем вакансии по минимальной зарплате
    filtered_vacancies_two = [vacancy for vacancy in filtered_vacancies
                              if vacancy.salary_from and
                              vacancy.salary_from >= min_salary]
    return filtered_vacancies_two


def sort_vacancies(filtered_vacancies: list):
    # Сортируем отфильтрованные вакансии по минимальной зарплате (от большей к меньшей)
    sorted_vacancies = sorted(filtered_vacancies,
                              key=lambda x: (x.salary_from if x.salary_from is not None else -1),
                              reverse=True)
    return sorted_vacancies


def get_top_vacancies(filtered_vacancies: list, top_n: int):
    return filtered_vacancies[:top_n]


def print_top_vacancies(filtered_vacancies: list, top_n: int):
    if len(filtered_vacancies) < top_n:
        print(f"Есть {len(filtered_vacancies)} вакансии")
    else:
        for vacancy in filtered_vacancies[:top_n]:
            print(vacancy)
