from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

BASE_URL = "http://itpc-jeddah.sa/company_exportir/"
NUM_OF_PAGE = 17
DRIVER = webdriver.Chrome("chromedriver.exe")

LINKS_FILE = "new_list.txt"
DATA_FILE = "new_data.csv"


def create_link_list():
    DRIVER.get(BASE_URL)

    with open(LINKS_FILE, "a") as f:
        p = 1

        while p <= NUM_OF_PAGE:
            content = DRIVER.page_source
            soup = BeautifulSoup(content, "html.parser")
            table = soup.find("table", {"id": "DataTables_Table_0"})
            sector_list = table.find_all("td", {"class": "sorting_1"})

            for s in sector_list:
                company_list_link = s.find("a")["href"]
                print(company_list_link)
                f.write(company_list_link + "\n")

            WebDriverWait(DRIVER, 20).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a#DataTables_Table_0_next")
                )
            ).click()

            p += 1


def get_company_info(company_link):
    DRIVER.get(company_link)
    company_info_content = DRIVER.page_source
    company_info_soup = BeautifulSoup(company_info_content, "html.parser")
    company_name = company_info_soup.find("h1", {"class": "entry-title"}).text.strip()
    company_details = company_info_soup.find_all("td")
    company_owner = company_details[0].text
    company_email = company_details[1].text
    company_phone = company_details[2].text
    company_web = company_details[3].text
    company_mobile = company_details[4].text
    company_address = company_details[6].text

    return [
        company_link,
        company_name,
        company_owner,
        company_email,
        company_phone,
        company_mobile,
        company_web,
        company_address,
    ]


def main():
    create_link_list()

    with open(LINKS_FILE, "r") as f:
        links = f.readlines()

    with open(DATA_FILE, "a+", newline="") as f:
        writer = csv.writer(f)

        for link in links:
            link = link.strip()
            DRIVER.get(link)
            company_list_content = DRIVER.page_source
            company_soup = BeautifulSoup(company_list_content, "html.parser")
            company_table = company_soup.find("table", {"id": "DataTables_Table_0"})
            company_list = company_table.find_all("td", {"class": "sorting_1"})

            for company in company_list:
                company_link = company.find("a")["href"]
                company_data = get_company_info(company_link)
                writer.writerow(company_data)
                print(company_data)

    DRIVER.quit()


if __name__ == "__main__":
    main()
