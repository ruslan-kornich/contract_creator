import requests
from bs4 import BeautifulSoup

from contract.services.director_name import short_director_name


def get_fop_info(code: str) -> dict:
    url = f"https://clarity-project.info/edr/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        main_div = soup.find("div", class_="entity-content").find_all("td")
        raw_short_name = " ".join(main_div[3].text.replace('"', "«").split())
        short_name = raw_short_name[:-1] + "»"
        full_name = short_name.replace("ФОП", "ФІЗИЧНА ОСОБА-ПІДПРИЄМЕЦЬ")
        code_company = main_div[1].text.lstrip()
        address = " ".join(
            main_div[7].find("div").text.replace("Запис в ЄДР:", "").split()[1:]
        )
        director = main_div[11].find("div").find("a").text.lstrip()
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
