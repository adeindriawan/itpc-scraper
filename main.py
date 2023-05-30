from selenium import webdriver
from bs4 import BeautifulSoup

base_url = "http://itpc-jeddah.sa/company_exportir/"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(base_url)
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
table = soup.find("table", {"id": "DataTables_Table_0"})
sector_list = table.find_all('td', {'class': 'sorting_1'})
for s in sector_list:
    # print(s.find('a')['href'])
    company_list_link = s.find('a')['href']
    driver.get(company_list_link)
    company_list_content = driver.page_source
    company_soup = BeautifulSoup(company_list_content, 'html.parser')
    company_table = company_soup.find("table", {"id": "DataTables_Table_0"})
    company_list = company_table.find_all('td', {'class': 'sorting_1'})
    for c in company_list:
        print(c.find('a')['href'])

# print(company_list)