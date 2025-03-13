import csv
import concurrent.futures
import datetime
import os
import requests
import re
from threading import Lock

from bs4 import BeautifulSoup

# import pandas as pd

import mysql.connector

lock = Lock()

finaloutput = []

def get_soup(url):
    print(url)
    cookies = {
        "visid_incap_2434933": "uUBGyMpCQIu9ukP/gwjE4ur8tWQAAAAAQUIPAAAAAADsq9FIH3fqEZmPgLm2m7zp",
        "bc_tstgrp": "5",
        "_gcl_au": "1.1.962787861.1689648368",
        "_ga": "GA1.1.1021046148.1689648368",
        "EQBHOME": "2",
        "nlbi_2434933": "kji3awpFhW2JjGv9iwf9swAAAABg4hoZ41W9Yk8QOorkDK7J",
        "incap_ses_959_2434933": "esx2L/BQZRPa+J4McA5PDdDT5GQAAAAAQAE6eWKQ/+HUw7tdz0YXoA==",
        "_ga_0QKFZ47KCP": "GS1.1.1692718033.8.0.1692718033.0.0.0",
        "_ga_9X00MVD9VR": "GS1.1.1692718033.8.0.1692718033.60.0.0",
        "nlbi_2434933_2147483392": "vxUQKKnVa0oMoYMiiwf9swAAAADpiikQyXS8VMqFECMqpYtp",
        "reese84": "3:VJs3Bk3I93VQL2k1TZQGrg==:97OYgWdTj45vxvcN66z3/6XqcB2UfROII/pr+RUfupSZZ4Ee2uUcxodDVGYbtrzZPy4tIQQOWpaMb9z9kmeQrxnC6LwHOXJfJeJcEey+aiuPPruMfwzbxmeSl/I6bzfNFUsPpkaNXVFTaMnoWCVNVhqsdPltei98u0dzlzPWHIq7S6ihZ3NxzLgwh67ZQ6hOOr8RExhtginAdYhhMMlGORu7g+Nou2Rsx5wQ56xahgLBHA3xLu6Vuurh6Aco4GHIPyFUYhClruJNphegqp9KuYW4369Ifsra0SeWHfPoclvJOOsNlGcC86h6T001k++ZRZwQKAk7RvE/sTU8y/9QYM9q6r+XgQhngocriTPaosV+CeCNjIVz4CtcGpoKpMQdefV6H9N0GRY1qeb40khGZ4dzGf/1Vxbl68qjYOPPecIKMXI8zspnHL7QEiPsIj/tHqw0xXZ38Pw1ZHGwuYnGQw==:HrlEh/ZxEorH7JxKgakVlHgq1ih7HX73UjuZqvugPd4=",
        "BCSessionID": "3b64eb55-267b-4d0c-aaa0-c7a129b880e4",
    }

    headers = {
        "authority": "www.equibase.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        # 'cookie': 'visid_incap_2434933=uUBGyMpCQIu9ukP/gwjE4ur8tWQAAAAAQUIPAAAAAADsq9FIH3fqEZmPgLm2m7zp; bc_tstgrp=5; _gcl_au=1.1.962787861.1689648368; _ga=GA1.1.1021046148.1689648368; EQBHOME=2; nlbi_2434933=kji3awpFhW2JjGv9iwf9swAAAABg4hoZ41W9Yk8QOorkDK7J; incap_ses_959_2434933=esx2L/BQZRPa+J4McA5PDdDT5GQAAAAAQAE6eWKQ/+HUw7tdz0YXoA==; _ga_0QKFZ47KCP=GS1.1.1692718033.8.0.1692718033.0.0.0; _ga_9X00MVD9VR=GS1.1.1692718033.8.0.1692718033.60.0.0; nlbi_2434933_2147483392=vxUQKKnVa0oMoYMiiwf9swAAAADpiikQyXS8VMqFECMqpYtp; reese84=3:VJs3Bk3I93VQL2k1TZQGrg==:97OYgWdTj45vxvcN66z3/6XqcB2UfROII/pr+RUfupSZZ4Ee2uUcxodDVGYbtrzZPy4tIQQOWpaMb9z9kmeQrxnC6LwHOXJfJeJcEey+aiuPPruMfwzbxmeSl/I6bzfNFUsPpkaNXVFTaMnoWCVNVhqsdPltei98u0dzlzPWHIq7S6ihZ3NxzLgwh67ZQ6hOOr8RExhtginAdYhhMMlGORu7g+Nou2Rsx5wQ56xahgLBHA3xLu6Vuurh6Aco4GHIPyFUYhClruJNphegqp9KuYW4369Ifsra0SeWHfPoclvJOOsNlGcC86h6T001k++ZRZwQKAk7RvE/sTU8y/9QYM9q6r+XgQhngocriTPaosV+CeCNjIVz4CtcGpoKpMQdefV6H9N0GRY1qeb40khGZ4dzGf/1Vxbl68qjYOPPecIKMXI8zspnHL7QEiPsIj/tHqw0xXZ38Pw1ZHGwuYnGQw==:HrlEh/ZxEorH7JxKgakVlHgq1ih7HX73UjuZqvugPd4=; BCSessionID=3b64eb55-267b-4d0c-aaa0-c7a129b880e4',
        "if-modified-since": "Tue, 22 Aug 2023 15:21:17 GMT",
        "if-none-match": '"64e4d26d-c6e9b"',
        "referer": "https://www.fiverr.com/",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
        proxies={
            "http": "http://f93287b8e75f42f5bf7d9c76130c4219:@proxy.crawlera.com:8011/",
            "https": "http://f93287b8e75f42f5bf7d9c76130c4219:@proxy.crawlera.com:8011/",
        },
        verify="zyte-proxy-ca.crt",
    )

    return BeautifulSoup(response.text, "html.parser")


def get(url, sel):
    for i in range(10):
        soup = get_soup(url)

        if soup.select(sel):
            return soup


def convert_to_datetime(date_str):
    return datetime.datetime.strptime(date_str, "%B %d, %Y")


def parse_race(race_soup, writer, raw_race):
    race_data = race_soup.select(".contenders .row")

    for contender in race_data:
        with open("a.html", "w") as f:
            f.write(str(contender))
        if not contender.select_one("h4 a"):
            continue

        horse = raw_race.copy()

        horse_name = contender.select_one("h4 a")
        horse["Horse Name"] = horse_name.get_text(strip=True)
        horse["Horse Reference No"] = re.findall(
            "refno=(.*?)®", horse_name.get("href")
        )[0]

        trainer = contender.select_one('div:-soup-contains("Trainer")')
        try:
            horse["Trainer"] = (
                trainer.get_text(strip=True).replace("Trainer:", "").strip()
            )
        except:
            pass

        try:
            horse["Trainer ID"] = re.findall(
                "ID=(.*?)&", trainer.select_one("a").get("href")
            )[0]
        except:
            pass

        jockey = contender.select_one('div:-soup-contains("Jockey:")')
        try:
            # horse["Jockey"] = jockey.select_one("a").get_text(strip=True)
            horse["Jockey"] = jockey.get_text(strip=True).replace("Jockey:", "").strip()
        except:
            pass

        try:
            horse["Jockey ID"] = re.findall(
                r"ID=(.*?)&", jockey.select_one("a").get("href")
            )[0]
        except:
            pass

        owner = contender.select_one('div:-soup-contains("Owner")')
        try:
            # horse["Owner"] = owner.select_one("a").get_text(strip=True)
            horse["Owner"] = owner.get_text(strip=True).replace("Owner:", "").strip()
        except:
            pass

        try:
            horse["Owner ID"] = re.findall(
                "ID=(.*?)&", owner.select_one("a").get("href")
            )[0]
        except:
            pass

        try:
            sire_dam_damsire = contender.select_one("h4 + p").get_text(strip=True)
        except:
            pass

        try:
            horse["Sire"] = re.findall(r"\((.*?)-", sire_dam_damsire)[0].strip()
        except:
            pass

        try:
            horse["Dam"] = re.findall(r"-(.*?),", sire_dam_damsire)[0].strip()
        except:
            pass

        try:
            horse["Dam Sire"] = re.findall(r" by (.*?)\)", sire_dam_damsire)[0].strip()
        except:
            pass

        try:
            horse["Breeder"] = (
                contender.select_one('div:-soup-contains("Breeder")')
                .get_text()
                .replace("Breeder:", "")
                .strip()
            )
        except:
            pass

        try:
            pp_text = (
                contender.select_one('div:-soup-contains("Post Postion:")')
                .get_text()
                .split("\n")
            )
            for text in pp_text:
                if "Post Postion:" in text:
                    horse["PP"] = text.replace("Post Postion:", "").strip()
                elif "M/L Odds:" in text:
                    horse["ML Odds"] = text.replace("M/L Odds:", "").strip()
        except:
            pass

        try:
            age_text = (
                contender.select_one('div:-soup-contains("Age: ")')
                .get_text()
                .split("\n")
            )

            for text in age_text:
                if "Age:" in text:
                    horse["Age"] = text.replace("Age:", "").strip()
                elif "Sex:" in text:
                    horse["Sex"] = text.replace("Sex:", "").strip()
                elif "Weight:" in text:
                    horse["Weight"] = text.replace("Weight:", "").strip()
                elif "Med:" in text:
                    horse["Med"] = text.replace("Med:", "").strip()
                elif "Claim:" in text:
                    horse["Claim"] = text.replace("Claim:", "").strip()

        except:
            pass

        with lock:
            # print(horse)
            finaloutput.append(horse)
            # writer.writerow(horse)


def parse_race_thread(startComp, url, writer):
    race_id = re.findall("RaceCardIndex(.*?)\.", url.get("href"))[0]
    # race_id = re.findall('RaceCardIndex(.*?)\.', url)[0]

    key = re.findall("[0-7]", re.findall(r"(.)-", race_id)[0])
    if key:
        _id = race_id.split("-")

        race_id = _id[0][:-1] + "-" + _id[1]

    url = f"https://www.equibase.com/static/entry/{race_id}.html"
    race_soup = get(url, ".phone-show.raceData")

    todaysdate = datetime.date.today()

    for race in race_soup.select(".phone-show.raceData"):
        raw_race = {}

        raw_race["Track ID"] = re.findall(f"([A-Z].*?)[0-9]", race_id)[0]
        raw_race["Area ID"] = re.findall(f"[0-9]([A-Z].*?)-", race_id)[0]
        raw_race["Race Date"] = race_soup.select_one(".race-date").text.strip()

        date = convert_to_datetime(raw_race["Race Date"])
        raw_race["Race Month"] = date.month
        raw_race["Race Year"] = date.year
        raw_race["Race day"] = date.day
        raw_race["Race No"] = (
            race.select_one("[id*=Race]").get("id").replace("Race", "").strip()
        )

        comp = datetime.date(int(date.year), int(date.month), int(date.day))

        if comp > startComp and comp <= todaysdate:
            # print("COMP Date: ", comp)
            parse_race(race, writer, raw_race)


def crawl_races(writer):
    soup = get(
        "https://www.equibase.com/static/entry/index.html", ".results .entryLink"
    )

    mydb = mysql.connector.connect(
        host="aconway01.mysql.pythonanywhere-services.com",
        user="aconway01",
        password="Milton123!!",
        database="aconway01$handicapped",
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT racedate from equibaserunnerinfo ORDER BY racedate DESC LIMIT 1"
    )

    startCompdate = str(mycursor.fetchall()[0][0])

    temp = [int(x) for x in str(startCompdate).split("-")]

    startComp = datetime.date(temp[0], temp[1], temp[2])

    # startComp = datetime.date(2023, 9, 2)

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for url in soup.select(".results .entryLink"):
            future = executor.submit(parse_race_thread, startComp, url, writer)
            futures.append(future)

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    # for url in soup.select('.results .entryLink'):
    #     race_id = re.findall('RaceCardIndex(.*?)\.', url.get('href'))[0]

    #     url = f'https://www.equibase.com/static/entry/{race_id}.html'
    #     race_soup = get(url, '.phone-show.raceData')

    #     for race in race_soup.select('.phone-show.raceData'):
    #         raw_race = {}

    #         raw_race['Track ID'] = race_id[:3]
    #         raw_race['Area ID'] = race_id.split('-')[0][-3:]
    #         raw_race['Race Date'] = race_soup.select_one('.race-date').text.strip()

    #         date = convert_to_datetime(raw_race['Race Date'])
    #         raw_race['Race Month'] = date.month
    #         raw_race['Race Year'] = date.year
    #         raw_race['Race day'] = date.day

    #         parse_race(race, writer, raw_race)


def equibaserunnerinfoextract():
    fields = [
        "Track ID",
        "Area ID",
        "Race Date",
        "Race Year",
        "Race Month",
        "Race day",
        "Race No",
        "Horse Name",
        "Horse Reference No",
        "Jockey",
        "Jockey ID",
        "Trainer",
        "Trainer ID",
        "Owner",
        "Owner ID",
        "Sire",
        "Dam",
        "Dam Sire",
        "Breeder",
        "PP",
        "Age",
        "Sex",
        "Med",
        "Weight",
        "ML Odds",
        "Claim",
    ]

    with open("equibaserunnerinfo.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()

        crawl_races(writer)

        writer.writerows(finaloutput)
        # parse_race_thread('https://www.equibase.com/static/chart/summary/RaceCardIndexAQU112523USA-EQB.html', writer)


if __name__ == "__main__":
    equibaserunnerinfoextract()

    os.remove("a.html")
