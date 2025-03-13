import requests

from datetime import date

import mysql.connector

def equibasethoroughbredhorsesdaily():

    mydb = mysql.connector.connect(
        host="aconway01.mysql.pythonanywhere-services.com",
        user="aconway01",
        password="Milton123!!",
        database="aconway01$handicapped"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT raceyear from equibasethoroughbredhorses ORDER BY raceyear DESC LIMIT 1")

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
            deleteQuery = "delete from equibasethoroughbredhorses where raceyear ="+myyear
            mycursor.execute(deleteQuery)

        # for myyear in range(2018,2024):

        output = []

        check = -1

        for i in range(1, 10000):

            url = "https://www.equibase.com/Data.cfm/Stats/Horse/Year/Page?year="+str(myyear)+"&page=" + \
                str(i)+"&sort=EARNINGS&dir=A&list=N&category=A&attribute_total=1024&set=full&race_breed_type=TB&_=1658074346392"

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            myres = response.json()

            for val in myres['stats']:
                output.append(val)
                try:
                    winpercentage = str(val["winPercentage"]).strip()
                except:
                    winpercentage = ""
                try:
                    horsename = str(val["horseName"]).strip()
                except:
                    horsename = ""
                try:
                    referencenumber = str(val["referenceNumber"]).strip()
                except:
                    referencenumber = ""
                try:
                    earnings = str(val["earnings"]).strip()
                except:
                    earnings = ""
                try:
                    equibaserank = str(val["rank"]).strip()
                except:
                    equibaserank = ""
                try:
                    place = str(val["place"]).strip()
                except:
                    place = ""
                try:
                    sirereference = str(val["sireReferenceNumber"]).strip()
                except:
                    sirereference = ""
                try:
                    equibasestarts = str(val["starts"]).strip()
                except:
                    equibasestarts = ""
                try:
                    sirename = str(val["sireName"]).strip()
                except:
                    sirename = ""
                try:
                    speedfigure = str(val["speedFigure"]).strip()
                except:
                    speedfigure = ""
                try:
                    perstart = str(val["perStart"]).strip()
                except:
                    perstart = ""
                try:
                    topthreepercent = str(val["topThreePercentage"]).strip()
                except:
                    topthreepercent = ""
                try:
                    equibaseshow = str(val["show"]).strip()
                except:
                    equibaseshow = ""
                try:
                    win = str(val["win"]).strip()
                except:
                    win = ""
                try:
                    topthree = str(val["topThree"]).strip()
                except:
                    topthree = ""
                try:
                    registry = str(val["registry"]).strip()
                except:
                    registry = ""

                raceyear = str(myyear)

                if horsename != "":

                    # # Insert record if not exists
                    # insertquery = "Insert into equibasethoroughbredhorses(raceyear,horsename,winpercentage,referencenumber,earnings,equibaserank,place,sirereference,equibasestarts,sirename,speedfigure,perstart,topthreepercent,equibaseshow,win,topthree,registry) \
                    #     select * from( Select %(raceyear)s as col0, %(horsename)s as col1, %(winpercentage)s as col2, %(referencenumber)s as col3, %(earnings)s as col4, %(equibaserank)s as col5, %(place)s as col6, %(sirereference)s as col7, %(equibasestarts)s as col8, %(sirename)s as col9, %(speedfigure)s as col10, %(perstart)s as col11, %(topthreepercent)s as col12, %(equibaseshow)s as col13, %(win)s as col14, %(topthree)s as col15, %(registry)s as col16) as temp \
                    #     where not exists \
                    #     (Select referencenumber from equibasethoroughbredhorses where raceyear=%(raceyear)s and horsename=%(horsename)s) LIMIT 1"

                    # Insert record
                    insertquery = "Insert into equibasethoroughbredhorses(raceyear,horsename,winpercentage,referencenumber,earnings,equibaserank,place,sirereference,equibasestarts,sirename,speedfigure,perstart,topthreepercent,equibaseshow,win,topthree,registry) \
                        select * from( Select %(raceyear)s as col0, %(horsename)s as col1, %(winpercentage)s as col2, %(referencenumber)s as col3, %(earnings)s as col4, %(equibaserank)s as col5, %(place)s as col6, %(sirereference)s as col7, %(equibasestarts)s as col8, %(sirename)s as col9, %(speedfigure)s as col10, %(perstart)s as col11, %(topthreepercent)s as col12, %(equibaseshow)s as col13, %(win)s as col14, %(topthree)s as col15, %(registry)s as col16) as temp"

                    mycursor.execute(insertquery, {'raceyear': raceyear, 'horsename': horsename, 'winpercentage': winpercentage, 'referencenumber': referencenumber, 'earnings': earnings, 'equibaserank': equibaserank, 'place': place, 'sirereference': sirereference,
                                    'equibasestarts': equibasestarts, 'sirename': sirename, 'speedfigure': speedfigure, 'perstart': perstart, 'topthreepercent': topthreepercent, 'equibaseshow': equibaseshow, 'win': win, 'topthree': topthree, 'registry': registry})

                    mycursor.execute("Commit")

                    # Update record if already exists
                    # updatequery = "UPDATE equibasethoroughbredhorses SET winpercentage = %(winpercentage)s, 'referencenumber': %(referencenumber)s, earnings = %(earnings)s, equibaserank = %(equibaserank)s, place = %(place)s, sirereference = %(sirereference)s, equibasestarts = %(equibasestarts)s, sirename = %(sirename)s, speedfigure = %(speedfigure)s, perstart = %(perstart)s, topthreepercent = %(topthreepercent)s, equibaseshow = %(equibaseshow)s, win = %(win)s, topthree = %(topthree)s, registry = %(registry)s WHERE raceyear = %(raceyear)s AND horsename = %(horsename)s"

                    # mycursor.execute(updatequery, {'raceyear': raceyear,'horsename': horsename, 'winpercentage': winpercentage, 'referencenumber': referencenumber, 'earnings': earnings, 'equibaserank': equibaserank, 'place': place, 'sirereference': sirereference,
                    #                 'equibasestarts': equibasestarts, 'sirename': sirename, 'speedfigure': speedfigure, 'perstart': perstart, 'topthreepercent': topthreepercent, 'equibaseshow': equibaseshow, 'win': win, 'topthree': topthree, 'registry': registry})

                    # mycursor.execute("Commit")

            # print("output: ", len(output))

            if check == len(output):
                break

            check = len(output)

        # mydf = pd.json_normalize(output)

        # mydf.to_csv('equibasethoroughbredhorses.csv', index=False)

    # Remove duplicates
    mycursor.execute("DELETE FROM equibasethoroughbredhorses WHERE equibasethoroughbredhorses_id IN(SELECT * FROM (SELECT MIN(equibasethoroughbredhorses_id) FROM equibasethoroughbredhorses GROUP BY raceyear, horsename HAVING COUNT(equibasethoroughbredhorses_id) > 1) temp);")
    mycursor.execute("Commit")


if __name__ == '__main__':

    equibasethoroughbredhorsesdaily()
