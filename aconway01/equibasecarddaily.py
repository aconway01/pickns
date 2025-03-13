import requests
# import pandas as pd
from datetime import date, timedelta, datetime

import mysql.connector


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)


def equibasecard():

    mydb = mysql.connector.connect(
        host="aconway01.mysql.pythonanywhere-services.com",
        user="aconway01",
        password="Milton123!!",
        database="aconway01$handicapped"
    )

    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT carddate from equibasecard ORDER BY carddate DESC LIMIT 1")

    startComp = mycursor.fetchall()[0][0].strftime("%Y%m%d")

    print(startComp)

    mycursor.execute(
        "delete from equibasecarddaily"
    )

    mycursor.execute("Commit")

    start = date.today()-timedelta(14)
    end = date.today()

    # start = date(2022,7,1)
    # startComp = "20220630"

    start_date = start  # date.today()-timedelta(21) #date(2021, 6, 1)
    end_date = end  # date.today()-timedelta(1) #date(2021, 12, 31)

    for single_date in daterange(start_date, end_date):

        if single_date.strftime("%Y%m%d") > startComp:

            months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                      "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

            urlday = ""
            if int(single_date.day) < 10:
                urlday = "0" + str(single_date.day)
            else:
                urlday = str(single_date.day)
            urlmonth = months[int(single_date.month)-1]
            urlyear = str(single_date.year)

            myurl = "https://racelens.equibase.com/home/GetTrackRaceHorseList?strDate=" + \
                urlday+"-"+urlmonth+"-"+urlyear
            print(myurl)

            # url = https://racelens.equibase.com/home/GetTrackRaceHorseList?strDate=17-JUL-2022

            payload = {}
            headers = {}

            response = requests.request(
                "GET", myurl, headers=headers, data=payload)

            myres = response.json()['data']

            output = [['Track_Id', 'Track_Name', 'Area_Id', 'State', 'Track_Stage', 'is_bullring', 'xml_flag', 'isfeat', 'frank', 'Race_Number', 'Text', 'Description', 'Wager_Text', 'Total_Purse', 'Post_Time', 'Race_Time', 'Day_Eve', 'race_type_desc', 'max_claim_price', 'distance_unit', 'distance_id',
                       'distance_in_furlong', 'course_type', 'pub_val', 'distance_display', 'surface_display', 'breed_type', 'race_Type', 'age_restriction', 'class_rating', 'distance_unit_desc', 'Prog_No', 'Reg_No', 'Horse_Name', 'ct', 'Win_Per', 'ML_Odds', 'Scratch_Indicator', 'post_pos', 'breed_type']]

            for val in myres:
                for val2 in val['Track_Details']:
                    for val3 in val2['Race_List']:
                        for val4 in val3['Horse_Details']:

                            # myvals = [val2['Track_Id'], val2['Track_Name'], val2['Area_Id'], val2['State'], val2['Track_Stage'], val2['is_bullring'], val2['xml_flag'], val2['isfeat'], val2['frank'], val3['Race_Number'], val3['Text'], val3['Description'], val3['Wager_Text'], val3['Total_Purse'], val3['Post_Time'], val3['Race_Time'], val3['Day_Eve'], val3['race_type_desc'], val3['max_claim_price'], val3['distance_unit'], val3['distance_id'],
                            #           val3['distance_in_furlong'], val3['course_type'], val3['pub_val'], val3['distance_display'], val3['surface_display'], val3['breed_type'], val3['race_Type'], val3['age_restriction'], val3['class_rating'], val3['distance_unit_desc'], val4['Prog_No'], val4['Reg_No'], val4['Horse_Name'], val4['ct'], val4['Win_Per'], val4['ML_Odds'], val4['Scratch_Indicator'], val4['post_pos'], val4['breed_type']]
                            # output.append(myvals)

                            carddate = single_date
                            try:
                                Track_Id = str(val2['Track_Id']).strip()
                            except:
                                Track_Id = ""
                            try:
                                Track_Name = str(val2['Track_Name'])
                            except:
                                Track_Name = ""
                            try:
                                Area_Id = str(val2['Area_Id'])
                            except:
                                Area_Id = ""
                            try:
                                State = str(val2['State'])
                            except:
                                State = ""
                            try:
                                Track_Stage = str(val2['Track_Stage'])
                            except:
                                Track_Stage = ""
                            try:
                                is_bullring = str(val2['is_bullring'])
                            except:
                                is_bullring = ""
                            try:
                                xml_flag = str(val2['xml_flag'])
                            except:
                                xml_flag = ""
                            try:
                                isfeat = str(val2['isfeat'])
                            except:
                                isfeat = ""
                            try:
                                frank = str(val2['frank'])
                            except:
                                frank = ""
                            try:
                                Race_Number = str(val3['Race_Number'])
                            except:
                                Race_Number = ""
                            try:
                                EquibaseText = str(val3['Text'])
                            except:
                                EquibaseText = ""
                            try:
                                EquibaseDescription = str(val3['Description'])
                            except:
                                EquibaseDescription = ""
                            try:
                                Wager_Text = str(val3['Wager_Text'])
                            except:
                                Wager_Text = ""
                            try:
                                Total_Purse = str(val3['Total_Purse']).strip().replace(
                                    "$", "").replace(",", "")
                            except:
                                Total_Purse = ""
                            if Total_Purse == "":
                                Total_Purse = None
                            try:
                                Post_Time_Val = str(val3['Post_Time']).split(" ")
                            except:
                                Post_Time_Val = ""
                            try:
                                Race_Time_Val = str(val3['Race_Time']).split(" ")
                            except:
                                Race_Time_Val = ""
                            try:
                                Day_Eve = str(val3['Day_Eve'])
                            except:
                                Day_Eve = ""
                            try:
                                race_type_desc = str(val3['race_type_desc'])
                            except:
                                race_type_desc = ""
                            try:
                                max_claim_price = str(val3['max_claim_price']).strip().replace(
                                    "$", "").replace(",", "")
                            except:
                                max_claim_price = ""
                            if max_claim_price == "":
                                max_claim_price = None
                            try:
                                distance_unit = str(val3['distance_unit'])
                            except:
                                distance_unit = ""
                            try:
                                distance_id = str(val3['distance_id'])
                            except:
                                distance_id = ""
                            try:
                                distance_in_furlong = str(
                                    val3['distance_in_furlong'])
                            except:
                                distance_in_furlong = ""
                            try:
                                course_type = str(val3['course_type'])
                            except:
                                course_type = ""
                            try:
                                pub_val = str(val3['pub_val'])
                            except:
                                pub_val = ""
                            try:
                                distance_display = str(val3['distance_display'])
                            except:
                                distance_display = ""
                            try:
                                surface_display = str(val3['surface_display'])
                            except:
                                surface_display = ""
                            try:
                                race_breed_type = str(val3['breed_type'])
                            except:
                                race_breed_type = ""
                            try:
                                race_Type = str(val3['race_Type'])
                            except:
                                race_Type = ""
                            try:
                                age_restriction = str(val3['age_restriction'])
                            except:
                                age_restriction = ""
                            try:
                                class_rating = str(val3['class_rating'])
                            except:
                                class_rating = ""
                            try:
                                distance_unit_desc = str(
                                    val3['distance_unit_desc'])
                            except:
                                distance_unit_desc = ""
                            try:
                                Prog_No = str(val4['Prog_No'])
                            except:
                                Prog_No = ""
                            try:
                                Reg_No = str(val4['Reg_No'])
                            except:
                                Reg_No = ""
                            try:
                                Horse_Name = str(val4['Horse_Name'])
                            except:
                                Horse_Name = ""
                            try:
                                ct = str(val4['ct'])
                            except:
                                ct = ""
                            try:
                                Win_Per = str(val4['Win_Per'])
                            except:
                                Win_Per = ""
                            try:
                                ML_Odds = str(val4['ML_Odds'])
                            except:
                                ML_Odds = ""
                            try:
                                Scratch_Indicator = str(val4['Scratch_Indicator'])
                            except:
                                Scratch_Indicator = ""
                            try:
                                post_pos = str(val4['post_pos'])
                            except:
                                post_pos = ""
                            try:
                                breed_type = str(val4['breed_type'])
                            except:
                                breed_type = ""

                            postdateObj = str(datetime.strptime(str(Post_Time_Val[0].split("-")[1]) + " " + str(Post_Time_Val[0].split("-")[0]).replace(
                                " ", "0").replace('"', "") + " 20" + str(Post_Time_Val[0].split("-")[2].replace('"', "")), "%b %d %Y")).split(" ")[0].split("-")

                            Post_Time = datetime(int(postdateObj[0]), int(postdateObj[1]), int(postdateObj[2]), int(Post_Time_Val[1].split(
                                ":")[0]), int(Post_Time_Val[1].split(":")[1]), int(Post_Time_Val[1].split(":")[2]))

                            racedateObj = str(datetime.strptime(str(Race_Time_Val[0].split("-")[1]) + " " + str(Race_Time_Val[0].split("-")[0]).replace(
                                " ", "0").replace('"', "") + " 20" + str(Race_Time_Val[0].split("-")[2].replace('"', "")), "%b %d %Y")).split(" ")[0].split("-")

                            Race_Time = datetime(int(racedateObj[0]), int(racedateObj[1]), int(racedateObj[2]), int(Race_Time_Val[1].split(
                                ":")[0]), int(Race_Time_Val[1].split(":")[1]), int(Race_Time_Val[1].split(":")[2]))

                            insertquery = "Insert into equibasecard(carddate,Track_Id,Track_Name,Area_Id,EquibaseState,Track_Stage,is_bullring,xml_flag,isfeat,frank,Race_Number,EquibaseText,EquibaseDescription,Wager_Text,Total_Purse,Post_Time,Race_Time,Day_Eve,race_type_desc,max_claim_price,distance_unit,distance_id,distance_in_furlong,course_type,pub_val,distance_display,surface_display,race_breed_type,race_Type,age_restriction,class_rating,distance_unit_desc,Prog_No,Reg_No,Horse_Name,ct,Win_Per,ML_Odds,Scratch_Indicator,post_pos,breed_type) \
                                            select * from( Select %(carddate)s as col0,%(Track_Id)s as col1,%(Track_Name)s as col2,%(Area_Id)s as col3,%(EquibaseState)s as col4,%(Track_Stage)s as col5,%(is_bullring)s as col6,%(xml_flag)s as col7,%(isfeat)s as col8,%(frank)s as col9,%(Race_Number)s as col10,%(EquibaseText)s as col11,%(EquibaseDescription)s as col12,%(Wager_Text)s as col13,%(Total_Purse)s as col14,%(Post_Time)s as col15,%(Race_Time)s as col16,%(Day_Eve)s as col17,%(race_type_desc)s as col18,%(max_claim_price)s as col19,%(distance_unit)s as col20,%(distance_id)s as col21,%(distance_in_furlong)s as col22,%(course_type)s as col23,%(pub_val)s as col24,%(distance_display)s as col25,%(surface_display)s as col26,%(race_breed_type)s as col27,%(race_Type)s as col28,%(age_restriction)s as col29,%(class_rating)s as col30,%(distance_unit_desc)s as col31,%(Prog_No)s as col32,%(Reg_No)s as col33,%(Horse_Name)s as col34,%(ct)s as col35,%(Win_Per)s as col36,%(ML_Odds)s as col37,%(Scratch_Indicator)s as col38,%(post_pos)s as col39,%(breed_type)s as col40) as temp"

                            mycursor.execute(insertquery, {'carddate': carddate, 'Track_Id': Track_Id, 'Track_Name': Track_Name, 'Area_Id': Area_Id, 'EquibaseState': State, 'Track_Stage': Track_Stage, 'is_bullring': is_bullring, 'xml_flag': xml_flag, 'isfeat': isfeat, 'frank': frank, 'Race_Number': Race_Number, 'EquibaseText': EquibaseText, 'EquibaseDescription': EquibaseDescription, 'Wager_Text': Wager_Text, 'Total_Purse': Total_Purse, 'Post_Time': Post_Time, 'Race_Time': Race_Time, 'Day_Eve': Day_Eve, 'race_type_desc': race_type_desc, 'max_claim_price': max_claim_price, 'distance_unit': distance_unit,
                                                           'distance_id': distance_id, 'distance_in_furlong': distance_in_furlong, 'course_type': course_type, 'pub_val': pub_val, 'distance_display': distance_display, 'surface_display': surface_display, 'race_breed_type': race_breed_type, 'race_Type': race_Type, 'age_restriction': age_restriction, 'class_rating': class_rating, 'distance_unit_desc': distance_unit_desc, 'Prog_No': Prog_No, 'Reg_No': Reg_No, 'Horse_Name': Horse_Name, 'ct': ct, 'Win_Per': Win_Per, 'ML_Odds': ML_Odds, 'Scratch_Indicator': Scratch_Indicator, 'post_pos': post_pos, 'breed_type': breed_type})
                            mycursor.execute("Commit")

                            insertquery = "Insert into equibasecarddaily(carddate,Track_Id,Track_Name,Area_Id,EquibaseState,Track_Stage,is_bullring,xml_flag,isfeat,frank,Race_Number,EquibaseText,EquibaseDescription,Wager_Text,Total_Purse,Post_Time,Race_Time,Day_Eve,race_type_desc,max_claim_price,distance_unit,distance_id,distance_in_furlong,course_type,pub_val,distance_display,surface_display,race_breed_type,race_Type,age_restriction,class_rating,distance_unit_desc,Prog_No,Reg_No,Horse_Name,ct,Win_Per,ML_Odds,Scratch_Indicator,post_pos,breed_type) \
                                            select * from( Select %(carddate)s as col0,%(Track_Id)s as col1,%(Track_Name)s as col2,%(Area_Id)s as col3,%(EquibaseState)s as col4,%(Track_Stage)s as col5,%(is_bullring)s as col6,%(xml_flag)s as col7,%(isfeat)s as col8,%(frank)s as col9,%(Race_Number)s as col10,%(EquibaseText)s as col11,%(EquibaseDescription)s as col12,%(Wager_Text)s as col13,%(Total_Purse)s as col14,%(Post_Time)s as col15,%(Race_Time)s as col16,%(Day_Eve)s as col17,%(race_type_desc)s as col18,%(max_claim_price)s as col19,%(distance_unit)s as col20,%(distance_id)s as col21,%(distance_in_furlong)s as col22,%(course_type)s as col23,%(pub_val)s as col24,%(distance_display)s as col25,%(surface_display)s as col26,%(race_breed_type)s as col27,%(race_Type)s as col28,%(age_restriction)s as col29,%(class_rating)s as col30,%(distance_unit_desc)s as col31,%(Prog_No)s as col32,%(Reg_No)s as col33,%(Horse_Name)s as col34,%(ct)s as col35,%(Win_Per)s as col36,%(ML_Odds)s as col37,%(Scratch_Indicator)s as col38,%(post_pos)s as col39,%(breed_type)s as col40) as temp"

                            mycursor.execute(insertquery, {'carddate': carddate, 'Track_Id': Track_Id, 'Track_Name': Track_Name, 'Area_Id': Area_Id, 'EquibaseState': State, 'Track_Stage': Track_Stage, 'is_bullring': is_bullring, 'xml_flag': xml_flag, 'isfeat': isfeat, 'frank': frank, 'Race_Number': Race_Number, 'EquibaseText': EquibaseText, 'EquibaseDescription': EquibaseDescription, 'Wager_Text': Wager_Text, 'Total_Purse': Total_Purse, 'Post_Time': Post_Time, 'Race_Time': Race_Time, 'Day_Eve': Day_Eve, 'race_type_desc': race_type_desc, 'max_claim_price': max_claim_price, 'distance_unit': distance_unit,
                                                           'distance_id': distance_id, 'distance_in_furlong': distance_in_furlong, 'course_type': course_type, 'pub_val': pub_val, 'distance_display': distance_display, 'surface_display': surface_display, 'race_breed_type': race_breed_type, 'race_Type': race_Type, 'age_restriction': age_restriction, 'class_rating': class_rating, 'distance_unit_desc': distance_unit_desc, 'Prog_No': Prog_No, 'Reg_No': Reg_No, 'Horse_Name': Horse_Name, 'ct': ct, 'Win_Per': Win_Per, 'ML_Odds': ML_Odds, 'Scratch_Indicator': Scratch_Indicator, 'post_pos': post_pos, 'breed_type': breed_type})
                            mycursor.execute("Commit")

            # df = pd.DataFrame(output)

            # df.to_csv(str(single_date)+'_racelensTrackRaceHorseList.csv',index=False, header=False)


if __name__ == '__main__':

    equibasecard()