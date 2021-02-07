import urllib3
from bs4 import BeautifulSoup


def find_stepstone_jobs(title: str, city: str):
    """ BeautifulSoup4 web scraping for Stepstone """

    http = urllib3.PoolManager()
    url = f"https://www.stepstone.se/lediga-jobb-i-hela-{city}?q={title}"
    page = http.request("GET", url)

    soup = BeautifulSoup(page.data, "lxml")
    bodies = soup.find_all(attrs={"class": "description"}, limit=10)

    jobs = []

    for item in bodies:
        jobs.append(
            {
                "title": item.h5.a.string,
                "company": item.span.text,
                "location": item.find_all("span")[1].find_all("span")[1].text,
                "url": item.span.a["href"],
            }
        )

    return jobs


def find_monster_jobs(title: str, city: str):
    """ BeautifulSoup4 web scraping for Stepstone """

    http = urllib3.PoolManager()
    url = f"https://www.monster.se/jobb/sok/?q={title}&where={city}"
    page = http.request("GET", url)

    soup = BeautifulSoup(page.data, "lxml")
    bodies = soup.find_all(attrs={"class": "summary"}, limit=10)

    jobs = []

    for item in bodies:
        jobs.append(
            {
                "title": item.header.h2.a.text.strip("\n\r"),
                "company": item.find_all("div")[0].text.strip("\n\r"),
                "location": item.find_all("div")[1].text.strip("\n\r").strip(" \r\n "),
                "url": item.header.h2.a["href"],
            }
        )

    return jobs