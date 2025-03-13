import pandas as pd

import datetime

import mysql.connector


def mdy_to_date(d):
    try:
        ret_date = datetime.datetime.strptime(d, "%B %d, %Y").date()
    except:
        ret_date = datetime.datetime.strptime(d, "%d-%b-%y").date()
    return ret_date


def equibaserunnerinfoparse():
    runnerinfo_pd_temp = pd.read_csv("equibaserunnerinfo.csv")

    runnerinfo_pd = (
        runnerinfo_pd_temp.drop_duplicates().fillna("")
        .sort_values(by=["Race Date", "Track ID"])
    )

    trackids = [str(x) for x in runnerinfo_pd["Track ID"].tolist()]
    areaids = [str(x) for x in runnerinfo_pd["Area ID"].tolist()]
    racedates = [mdy_to_date(x) for x in runnerinfo_pd["Race Date"].tolist()]
    raceyears = [str(x) for x in runnerinfo_pd["Race Year"].tolist()]
    racemonths = [str(x) for x in runnerinfo_pd["Race Month"].tolist()]
    racedays = [str(x) for x in runnerinfo_pd["Race day"].tolist()]
    racenos = [str(x) for x in runnerinfo_pd["Race No"].tolist()]
    horsenames = [str(x) for x in runnerinfo_pd["Horse Name"].tolist()]
    horserefnos = [str(x) for x in runnerinfo_pd["Horse Reference No"].tolist()]
    jockeys = [str(x) for x in runnerinfo_pd["Jockey"].tolist()]
    jockeyids = [str(x) for x in runnerinfo_pd["Jockey ID"].tolist()]
    trainers = [str(x) for x in runnerinfo_pd["Trainer"].tolist()]
    trainerids = [str(x) for x in runnerinfo_pd["Trainer ID"].tolist()]
    owners = [str(x) for x in runnerinfo_pd["Owner"].tolist()]
    ownerids = [str(x) for x in runnerinfo_pd["Owner ID"].tolist()]
    sires = [str(x) for x in runnerinfo_pd["Sire"].tolist()]
    dams = [str(x) for x in runnerinfo_pd["Dam"].tolist()]
    damsires = [str(x) for x in runnerinfo_pd["Dam Sire"].tolist()]
    breeders = [str(x) for x in runnerinfo_pd["Breeder"].tolist()]
    pps = [str(x) for x in runnerinfo_pd["PP"].tolist()]
    ages = [str(x) for x in runnerinfo_pd["Age"].tolist()]
    sexes = [str(x) for x in runnerinfo_pd["Sex"].tolist()]
    meds = [str(x) for x in runnerinfo_pd["Med"].tolist()]
    weightsTemp = [
        str(x)[0:3] if int(x) > 999 and str(x)[0] == "1" else str(x)
        for x in runnerinfo_pd["Weight"].tolist()
    ]
    weights = [
        str(x)[0:2]
        if int(x) >= 100 and (str(x)[0] == "9" or str(x)[0] == "8" or str(x)[0] == "7")
        else str(x)
        for x in weightsTemp
    ]
    mloddes = [str(x) for x in runnerinfo_pd["ML Odds"].tolist()]
    claims = [
        str(x).replace("$", "").replace(",", "")
        for x in runnerinfo_pd["Claim"].tolist()
    ]

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

    mycursor.execute(
        "delete from equibaserunnerinfodaily"
    )

    mycursor.execute("Commit")

    # startComp = datetime.date(2023, 11, 30)

    if len(trackids) > 0:
        for i in range(len(trackids)):
            if racedates[i] > startComp:
                trackid = trackids[i]
                areaid = areaids[i]
                racedate = racedates[i]
                raceyear = raceyears[i]
                racemonth = racemonths[i]
                raceday = racedays[i]
                racenumber = racenos[i]
                horsename = horsenames[i]
                horserefno = horserefnos[i]
                jockeyname = jockeys[i]
                jockeyid = jockeyids[i]
                trainername = trainers[i]
                trainerid = trainerids[i]
                ownername = owners[i]
                ownerid = ownerids[i]
                sirename = sires[i]
                damname = dams[i]
                damsirename = damsires[i]
                breeder = breeders[i]
                pp = pps[i]
                age = ages[i]
                sex = sexes[i]
                med = meds[i]
                jockeyweight = weights[i]
                mlodds = mloddes[i]
                claim = claims[i]

                try:
                    #  Insert record
                    insertquery = "Insert into equibaserunnerinfo(trackid,areaid,racedate,raceyear,racemonth,raceday,racenumber,horsename,horserefno,jockeyname,jockeyid,trainername,trainerid,ownername,ownerid,sirename,damname,damsirename,breeder,pp,age,sex,med,jockeyweight,mlodds,claim) \
                        select * from( Select %(trackid)s as col0, %(areaid)s as col1, %(racedate)s as col2, %(raceyear)s as col3, %(racemonth)s as col4, %(raceday)s as col5, %(racenumber)s as col6, %(horsename)s as col7, %(horserefno)s as col8, %(jockeyname)s as col9, %(jockeyid)s as col10, %(trainername)s as col11, %(trainerid)s as col12, %(ownername)s as col13, %(ownerid)s as col14, %(sirename)s as col15, %(damname)s as col16, %(damsirename)s as col17, %(breeder)s as col18, %(pp)s as col19, %(age)s as col20, %(sex)s as col21, %(med)s as col22, %(jockeyweight)s as col23, %(mlodds)s as col24, %(claim)s as col25) as temp"

                    mycursor.execute(
                        insertquery,
                        {
                            "trackid": trackid,
                            "areaid": areaid,
                            "racedate": racedate,
                            "raceyear": raceyear,
                            "racemonth": racemonth,
                            "raceday": raceday,
                            "racenumber": racenumber,
                            "horsename": horsename,
                            "horserefno": horserefno,
                            "jockeyname": jockeyname,
                            "jockeyid": jockeyid,
                            "trainername": trainername,
                            "trainerid": trainerid,
                            "ownername": ownername,
                            "ownerid": ownerid,
                            "sirename": sirename,
                            "damname": damname,
                            "damsirename": damsirename,
                            "breeder": breeder,
                            "pp": pp,
                            "age": age,
                            "sex": sex,
                            "med": med,
                            "jockeyweight": jockeyweight,
                            "mlodds": mlodds,
                            "claim": claim,
                        },
                    )

                    mycursor.execute("Commit")

                    #  Insert record
                    insertquery = "Insert into equibaserunnerinfodaily(trackid,areaid,racedate,raceyear,racemonth,raceday,racenumber,horsename,horserefno,jockeyname,jockeyid,trainername,trainerid,ownername,ownerid,sirename,damname,damsirename,breeder,pp,age,sex,med,jockeyweight,mlodds,claim) \
                        select * from( Select %(trackid)s as col0, %(areaid)s as col1, %(racedate)s as col2, %(raceyear)s as col3, %(racemonth)s as col4, %(raceday)s as col5, %(racenumber)s as col6, %(horsename)s as col7, %(horserefno)s as col8, %(jockeyname)s as col9, %(jockeyid)s as col10, %(trainername)s as col11, %(trainerid)s as col12, %(ownername)s as col13, %(ownerid)s as col14, %(sirename)s as col15, %(damname)s as col16, %(damsirename)s as col17, %(breeder)s as col18, %(pp)s as col19, %(age)s as col20, %(sex)s as col21, %(med)s as col22, %(jockeyweight)s as col23, %(mlodds)s as col24, %(claim)s as col25) as temp"

                    mycursor.execute(
                        insertquery,
                        {
                            "trackid": trackid,
                            "areaid": areaid,
                            "racedate": racedate,
                            "raceyear": raceyear,
                            "racemonth": racemonth,
                            "raceday": raceday,
                            "racenumber": racenumber,
                            "horsename": horsename,
                            "horserefno": horserefno,
                            "jockeyname": jockeyname,
                            "jockeyid": jockeyid,
                            "trainername": trainername,
                            "trainerid": trainerid,
                            "ownername": ownername,
                            "ownerid": ownerid,
                            "sirename": sirename,
                            "damname": damname,
                            "damsirename": damsirename,
                            "breeder": breeder,
                            "pp": pp,
                            "age": age,
                            "sex": sex,
                            "med": med,
                            "jockeyweight": jockeyweight,
                            "mlodds": mlodds,
                            "claim": claim,
                        },
                    )

                    mycursor.execute("Commit")

                except:
                    print("Failed to insert:")
                    print(
                        trackids[i],
                        areaids[i],
                        racedates[i],
                        raceyears[i],
                        racemonths[i],
                        racedays[i],
                        racenos[i],
                        horsenames[i],
                        horserefnos[i],
                        jockeys[i],
                        jockeyids[i],
                        trainers[i],
                        trainerids[i],
                        owners[i],
                        ownerids[i],
                        sires[i],
                        dams[i],
                        damsires[i],
                        breeders[i],
                        pps[i],
                        ages[i],
                        sexes[i],
                        meds[i],
                        weights[i],
                        mloddes[i],
                        claims[i],
                        sep=",",
                    )
                    print()


if __name__ == "__main__":
    equibaserunnerinfoparse()
