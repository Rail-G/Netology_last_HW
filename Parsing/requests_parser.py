import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def hh_parser(
    text: str,
    area: int | list,
):
    stradania = []
    count = 0
    count_vacancy = 0
    while True:
        if count == 1:  # --> Ограничение на 3 страницы.
            break
        params = {"text": text, "area": area, "page": count}
        useragent = UserAgent()
        headers = {"User-Agent": useragent.edge}
        url = "https://kazan.hh.ru/search/vacancy?"
        response = requests.get(url=url, params=params, headers=headers)
        if (
            response.status_code == 404
        ):  # --> Если бы все существующие страницы пришлось бы проверять. У меня ушло ~9 минут :(
            print("Конец страницы")
            break
        soup = BeautifulSoup(response.text, "lxml")
        vacancy = soup.find("div", id="a11y-main-content")
        serp_item = vacancy.find_all("div", class_="serp-item")
        for href_title in serp_item:
            href = href_title.find("a")["href"]
            vac = requests.get(href, headers=headers)
            soup2 = BeautifulSoup(vac.text, "lxml")
            maxx = soup2.find("div", class_="g-user-content")
            max = maxx.get_text() if maxx else '1' # --> БЫли моменты когда вызывал ошибку NoneType. По этому добавил if/else.
            if "Django" in max or "Flask" in max:
                count_vacancy += 1
                city = href_title.find(
                    "div", {"data-qa": "vacancy-serp__vacancy-address"}
                ).get_text()
                zps = href_title.find("span", class_="bloko-header-section-2")
                zpf = zps.get_text() if zps else "Зарплата не указана"
                com = href_title.find(
                    "a", class_="bloko-link bloko-link_kind-tertiary"
                ).get_text()
                dict_ = {"City": city, "Salary": zpf, "Company": com, "Link": href}
                stradania.append(dict_)
        count += 1
    with open("gigafile.json", "w", encoding="utf-8") as file:
        json.dump(stradania, file, ensure_ascii=False, indent=2)
    return 'Вакансии добавлены в количестве {} штук. Удачного собеседования!'.format(count_vacancy)

def main():
    text = 'python'
    area = [1, 2]
    print(hh_parser(text, area))

if __name__ == '__main__':
    main()
