

class Vacancy:
    def __init__(self, name, company_name, area, url, snippet_req, salary_from, salary_to, currency):
        self.name = name
        self.company_name = company_name
        self.area = area
        self.url = url
        self.snippet_req = snippet_req
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self):
        return (f'{self.name}\n'
                f'Компания: {self.company_name}\n'
                f'Город {self.area}\n'
                f'Ссылка на вакансию: {self.url}\n'
                f'{self.snippet_req}\n'
                f'ЗП от {self.salary_from} до {self.salary_to} {self.currency}\n')

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return False
        return (self.name == other.name and
                self.company_name == other.company_name and
                self.area == other.area and
                self.url == other.url and
                self.snippet_req == other.snippet_req and
                self.salary_from == other.salary_from and
                self.salary_to == other.salary_to and
                self.currency == other.currency)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise ValueError("не является классом Vacancy")
        return self.salary_from < other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise ValueError("не является классом Vacancy")
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise ValueError("не является классом Vacancy")
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise ValueError("Cannot compare Vacancy with non-Vacancy object.")
        return self.salary_from >= other.salary_from

    @staticmethod
    def cast_to_object_list(hh_vacancies):
        """
        Сортировка по зп,
        если зп не указано,
        то пропускаем вакансию
        :param hh_vacancies:
        :return:
        """
        vacancies = []
        for i in hh_vacancies:
            name = i.get('name', 'Не указано')
            company_name = i.get('employer', {}).get('name', 'Не указано')
            area = i.get('area', {}).get('name', 'Не указано')
            url = i.get('alternate_url', 'Ссылка не доступна')
            snippet_req = i.get('snippet', {}).get('requirement', 'Описание не доступно')
            salary_data = i.get('salary')
            # Проверяем наличие данных о зарплате
            if salary_data:
                salary_from = salary_data.get('from', " ")
                salary_to = salary_data.get('to', " ")
                currency = salary_data.get('currency', " ")
                # Пропускаем вакансию, если хотя бы одно из значений зарплаты отсутствует
                if salary_from is None or salary_to is None or currency is None:
                    continue
            else:
                # Пропускаем вакансию, если данные о зарплате отсутствуют
                continue
            vac = Vacancy(name, company_name, area, url, snippet_req, salary_from, salary_to, currency)
            vacancies.append(vac)
        return vacancies
