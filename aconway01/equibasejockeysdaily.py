import requests

from datetime import date

import mysql.connector

def equibasejockeysdaily():

    mydb = mysql.connector.connect(
        host="aconway01.mysql.pythonanywhere-services.com",
        user="aconway01",
        password="Milton123!!",
        database="aconway01$handicapped"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT raceyear from equibasejockeys ORDER BY raceyear DESC LIMIT 1")

    startComp = str(mycursor.fetchall()[0][0])

    print(startComp)

    todays_date = date.today()

    myyear = str(todays_date.year)

    # myday = str(todays_date.day)

    myweekday = str(todays_date.weekday())

    # print(myday)

    # checkday = ["1","15"]

    print(myweekday)

    checkweekday = ["0"]

    # if myday in checkday:

    if myweekday in checkweekday:

        if startComp == myyear:
            deleteQuery = "delete from equibasejockeys where raceyear ="+myyear
            mycursor.execute(deleteQuery)

        # for myyear in range(2012,2024):

        output = []

        check = -1

        for i in range(1,1000):

            url = "https://www.equibase.com/Data.cfm/Stats/Jockey/Year/Page?year="+str(myyear)+"&list=N&sort=EARNINGS&dir=A&page="+str(i)+"&set=full&attribute_total=1024&race_breed_type=TB&_=1658103981195"

            payload={}
            headers = {
            'Cookie': 'incap_ses_8222_2434933=GrOlV/tbJiUSA5pHzWkacsWo1GIAAAAAQBQgdrC52qEzAPSawskM3A==; nlbi_2434933=/Tr+CvecmXnF2oJoiwf9swAAAACGYXv925CzTAJaX526Lxa8; visid_incap_2434933=DYVvZpC5TH+UAJnJeNz7uPox1GIAAAAAQUIPAAAAAACcCEXDLw0ILluJaeCxlFs0'
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            myres = response.json()

            for val in myres['stats']:
                output.append(val)
                try:
                    winpercentage = str(val["winPercentage"])
                except:
                    winpercentage = ""
                try:
                    jockeyname = str(val["jockeyName"])
                except:
                    jockeyname = ""
                try:
                    earnings = str(val["earnings"])
                except:
                    earnings = ""
                try:
                    equibaserank = str(val["rank"])
                except:
                    equibaserank = ""
                try:
                    place = str(val["place"])
                except:
                    place = ""
                try:
                    equibaseidentity = str(val["identity"])
                except:
                    equibaseidentity = ""
                try:
                    equibasestarts = str(val["starts"])
                except:
                    equibasestarts = ""
                try:
                    perstart = str(val["perStart"])
                except:
                    perstart = ""
                try:
                    topthreepercent = str(val["topThreePercentage"])
                except:
                    topthreepercent = ""
                try:
                    equibaseshow = str(val["show"])
                except:
                    equibaseshow = ""
                try:
                    win = str(val["win"])
                except:
                    win = ""
                try:
                    topthree = str(val["topThree"])
                except:
                    topthree = ""

                raceyear = str(myyear)

                if jockeyname != "":

                    # Insert record
                    insertquery = "Insert into equibasejockeys(raceyear,jockeyname,winpercentage,equibaseidentity,earnings,equibaserank,place,equibasestarts,perstart,topthreepercent,equibaseshow,win,topthree) \
                        select * from( Select %(raceyear)s as col0, %(jockeyname)s as col1, %(winpercentage)s as col2, %(equibaseidentity)s as col3, %(earnings)s as col4, %(equibaserank)s as col5, %(place)s as col6, %(equibasestarts)s as col7, %(perstart)s as col8, %(topthreepercent)s as col9, %(equibaseshow)s as col10, %(win)s as col11, %(topthree)s as col12) as temp"

                    mycursor.execute(insertquery, {'raceyear': raceyear, 'jockeyname': jockeyname, 'winpercentage': winpercentage, 'equibaseidentity': equibaseidentity, 'earnings': earnings, 'equibaserank': equibaserank, 'place': place,
                                    'equibasestarts': equibasestarts, 'perstart': perstart, 'topthreepercent': topthreepercent, 'equibaseshow': equibaseshow, 'win': win, 'topthree': topthree})

                    mycursor.execute("Commit")

            # print("output: ",len(output))

            if check == len(output):
                break

            check = len(output)

        # mydf = pd.json_normalize(output)

        # mydf.to_csv('equibaseJockeys2022.csv',index=False)

    # Remove duplicates
    mycursor.execute("DELETE FROM equibasejockeys WHERE equibasejockeys_id IN(SELECT * FROM (SELECT MIN(equibasejockeys_id) FROM equibasejockeys GROUP BY raceyear, jockeyname HAVING COUNT(equibasejockeys_id) > 1) temp);")
    mycursor.execute("Commit")


if __name__ == '__main__':

    equibasejockeysdaily()