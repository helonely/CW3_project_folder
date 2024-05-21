import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        super().__init__()
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword: str):
        self.params['text'] = keyword
        query_vacancies = []
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            query_vacancies.extend(vacancies)
            self.params['page'] += 1
        return query_vacancies


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()

if __name__ == "__main__":
    # Получение вакансий с hh.ru в формате JSON
    hh_vacancies = hh_api.get_vacancies("Python")

    for i in hh_vacancies:
        print(i)
