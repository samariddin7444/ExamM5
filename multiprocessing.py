import os
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def save_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_name = url.split('/')[-1]
        with open(f"{page_name}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"{page_name} saqlandi.")
    else:
        print(f"Xatolik: {response.status_code}")

def main():
    base_url = "https://tilshunos.com/sinonims/"
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = [base_url + link.get('href') for link in soup.find_all('a') if link.get('href').startswith('sinonims')]
        pool = Pool(processes=os.cpu_count())
        pool.map(save_page, links)
        pool.close()
        pool.join()
    else:
        print(f"Xatolik: {response.status_code}")

if __name__ == "__main__":
    main()
