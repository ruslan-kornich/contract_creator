import requests
from bs4 import BeautifulSoup

from contract.services.director_name import short_director_name


def get_company_info(code: str) -> dict:
    url = f"https://opendatabot.ua/c/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        main_div = soup.find("div", class_="container bg-white shadow-sm rounded px-4")
        short_name = (
            main_div.find("div", class_="text-center")
            .find("h1")
            .text.replace("«", '"')
            .replace("»", '"')
        )
        raw_data_company = main_div.find("div", class_="text-center").find("h2").text
        code_company = "".join([i for i in raw_data_company if i.isdigit()])
        data = main_div.find("div", class_="row").find_all("div", class_="col-12 col")
        name_and_address = [i.find("p").text for i in data]
        full_name = (
            name_and_address[1].replace("«", '"').replace("»", '"').replace("­", "")
        )
        address = name_and_address[2]
        director = (
            main_div.find("div", class_="row")
            .find_all("div", class_="col-sm-4 col-6 col")[1]
            .text.replace("Директор", "")
        )
        final_data = dict(
            {
                "short_name": short_name,
                "code_company": code_company,
                "director": director,
                "short_dir_name": short_director_name(director),
                "full_name": full_name,
                "address": address,
            }
        )
        return final_data
    else:
        return {}
