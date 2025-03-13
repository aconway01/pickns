from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.urls import reverse_lazy

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
from django.db.models import IntegerField

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .models import Equibasecarddaily, Equibaserunnerinfodaily, Equibasethoroughbredhorses, Equibasejockeys, Equibasetrainers, Equibaseowners

import copy

myhost = "http://www.handicapped.io"

def money(val):
    return '${:,.2f}'.format(val)

def home(request):

    datetoday = datetime.today()-timedelta(hours=5)

    cards = Equibasecarddaily.objects.filter(
        Q(carddate=datetoday))

    tracknames = cards.values(
        'track_name', 'track_id', 'area_id', 'equibasestate').order_by('track_name').distinct()

    racenumbers = cards.values(
        'race_number').distinct()

    context = {
        'today': datetoday,
        'cards': cards,
        'tracknames': tracknames,
        'racenumbers': racenumbers,
    }

    return render(request, 'races/todaysraces.html', context)

# @login_required
def view_races(request, racedate, trackid):

    # datetoday = datetime.today() - timedelta(hours=5)

    datevals = racedate.split("-")

    datetoday = datetime(int(datevals[0]),int(datevals[1]),int(datevals[2]))

    cards = Equibasecarddaily.objects.filter(Q(carddate=datetoday) & Q(track_id=trackid))

    races = cards.values('track_id', 'race_number', 'total_purse', 'post_time', 'race_type_desc','distance_in_furlong', 'surface_display', 'race_breed_type').distinct()

    for race in races:
        try:
            race['totalpursefloat'] = float(race['total_purse'])
        except:
            race['totalpursefloat'] = 0.0
        race['total_purse'] = money(float(race['total_purse']))

    trackname = cards[0].track_name
    state = cards[0].equibasestate
    area_id = cards[0].area_id
    track_id = cards[0].track_id

    if int(datetoday.day) < 10:
        urlday = "0" + str(datetoday.day)
    else:
        urlday = str(datetoday.day)
    if int(datetoday.month) < 10:
        urlmonth = "0" + str(datetoday.month)
    else:
        urlmonth = str(datetoday.month)
    urlyear = str(datetoday.year)[2:4]

    context = {
        'myhost': myhost,
        'today': datetoday,
        'cards': cards,
        'trackname': trackname,
        'state': state,
        'area_id': area_id,
        'track_id': track_id,
        'races': races,
        'urlday': urlday,
        'urlmonth': urlmonth,
        'urlyear': urlyear,
    }

    return render(request, 'races/view_races.html', context)

# @login_required
def view_race(request, racedate, trackid, racenumber):

    # datetoday = datetime.today() - timedelta(hours=5)

    datevals = racedate.split("-")

    datetoday = datetime(int(datevals[0]),int(datevals[1]),int(datevals[2]))

    last3years = (datetoday - relativedelta(years=3)).year

    cards = Equibasecarddaily.objects.filter(Q(carddate=datetoday) & Q(track_id=trackid) & Q(race_number=racenumber)).annotate(my_integer_field=Cast('post_pos', IntegerField())).order_by('my_integer_field', 'post_pos')

    runnerinfo = Equibaserunnerinfodaily.objects.filter(Q(racedate=datetoday) & Q(trackid=trackid) & Q(racenumber=racenumber)).annotate(my_integer_field=Cast('pp', IntegerField())).order_by('my_integer_field', 'pp')

    race = cards.values('equibasestate', 'area_id', 'track_id', 'track_name', 'race_number', 'equibasetext', 'wager_text', 'total_purse', 'post_time', 'race_type_desc', 'distance_in_furlong', 'surface_display', 'race_breed_type').distinct()[0]

    race['total_purse'] = money(float(race['total_purse']))

    if int(datetoday.day) < 10:
        urlday = "0" + str(datetoday.day)
    else:
        urlday = str(datetoday.day)
    if int(datetoday.month) < 10:
        urlmonth = "0" + str(datetoday.month)
    else:
        urlmonth = str(datetoday.month)
    urlyear = str(datetoday.year)[2:4]

    # horsedatasets = [{
    #     label: "Mischievous Path",
    #     data: [
    #     {
    #         year: '2020', vals: {equibaserank: 1000, speed: 95}
    #     },
    #     {
    #         year: '2021', vals: {equibaserank: 940, speed: 92}
    #     },
    #     {
    #         year: '2022', vals: {equibaserank: 970, speed: 94}
    #     },
    #     ],
    #     borderWidth: 1,
    #     parsing: {
    #         xAxisKey: 'year',
    #         yAxisKey: 'vals.equibaserank'
    #     }
    #   },..]

    # horsedatasets = [{
    #    'label': "horsename",
    #    'data': [{
    #            'year': '2020',
    #            'vals': {'EQBrank': '940', 'speed': '94'}
    #        },
    #        {
    #            'year': '2021',
    #            'vals': {'EQBrank': '940', 'speed': '94'}
    #        },
    #        ]
    # }

    cardhorses = [x.horse_name for x in cards]

    for i in range(len(runnerinfo)):
        if str(runnerinfo[i].jockeyid) == "":
            runnerinfo[i].jockeyid = "0.0"
        if str(runnerinfo[i].trainerid) == "":
            runnerinfo[i].trainerid = "0.0"
        if str(runnerinfo[i].ownerid) == "":
            runnerinfo[i].ownerid = "0.0"

    runnerjockeys = [str(int(float(x.jockeyid))) if str(x.jockeyid) != "0.0" else str(x.jockeyid) for x in runnerinfo]

    runnertrainers = [str(int(float(x.trainerid))) if str(x.trainerid) != "0.0" else str(x.trainerid) for x in runnerinfo]

    runnerowners = [str(int(float(x.ownerid))) if str(x.ownerid) != "0.0" else str(x.ownerid)  for x in runnerinfo]

    equibasehorses = Equibasethoroughbredhorses.objects.filter(Q(horsename__in=cardhorses) & Q(raceyear__gte=last3years)).order_by('raceyear')

    equibasejockeys = Equibasejockeys.objects.filter(Q(equibaseidentity__in=runnerjockeys) & Q(raceyear__gte=last3years)).order_by('raceyear')

    equibasetrainers = Equibasetrainers.objects.filter(Q(equibaseidentity__in=runnertrainers) & Q(raceyear__gte=last3years)).order_by('raceyear')

    equibaseowners = Equibaseowners.objects.filter(Q(equibaseidentity__in=runnerowners) & Q(raceyear__gte=last3years)).order_by('raceyear')

    # Initialize datasets for each horse, jockey, trainer, owner
    horsedatasets = []
    jockeydatasets = []
    trainerdatasets = []
    ownerdatasets = []
    existing = []
    equibasehorsenames = [x.horsename for x in equibasehorses]
    runnerinfohorses = [str(x.horsename).split(" (")[0] for x in runnerinfo]
    runnerinfohorses2 = [x.horsename for x in runnerinfo]
    for card in cards:
        if card.horse_name not in existing:
            entry = {} # {'label': card.horse_name, 'my_integer_field': card.my_integer_field, 'scratch_indicator', card.scratch_indicator, 'data': []}
            entry['label'] = card.horse_name
            entry['my_integer_field'] = card.my_integer_field
            entry['scratch_indicator'] = card.scratch_indicator
            if card.horse_name in equibasehorsenames:
                entry['referencenumber'] = [x.referencenumber for x in equibasehorses if x.horsename == card.horse_name][0]
            else:
                entry['referencenumber'] = ""

            if card.horse_name in runnerinfohorses or card.horse_name in runnerinfohorses2:
                entry['jockeyname'] = [str(x.jockeyname) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['jockeyid'] = [str(int(float(x.jockeyid))) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['trainername'] = [str(x.trainername) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['trainerid'] = [str(int(float(x.trainerid))) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['ownername'] = [str(x.ownername) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                if len(str(entry['ownername'])) > 30:
                    entry['ownername'] = str(entry['ownername'])[0:29]+"..."
                entry['ownerid'] = [str(int(float(x.ownerid))) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['sirename'] = [str(x.sirename) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['damname'] = [str(x.damname) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['damsirename'] = [str(x.damsirename) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['breeder'] = [str(x.breeder) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                if len(str(entry['breeder'])) > 30:
                    entry['breeder'] = str(entry['breeder'])[0:29]+"..."
                entry['pp'] = [str(x.pp) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['age'] = [str(x.age) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['sex'] = [str(x.sex) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['med'] = [str(x.med).replace("1","") for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                entry['jockeyweight'] = [str(x.jockeyweight) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                # entry['mlodds'] = [x.mlodds for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
                # try:
                #     odds = str(x.mlodds).split("/")
                #     floatodds = int(odds[0])/int(odds[1])
                #     entry['mloddsfloat'] = floatodds
                # except:
                #     entry['mloddsfloat'] = 0.0
                entry['claim'] = [money(float(x.claim)) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            else:
                entry['jockeyname'] = ""
                entry['jockeyid'] = ""
                entry['trainername'] = ""
                entry['trainerid'] = ""
                entry['ownername'] = ""
                entry['ownerid'] = ""
                entry['sirename'] = ""
                entry['damname'] = ""
                entry['damsirename'] = ""
                entry['breeder'] = ""
                entry['pp'] = ""
                entry['age'] = ""
                entry['sex'] = ""
                entry['med'] = ""
                entry['jockeyweight'] = ""
                # entry['mlodds'] = ""
                entry['claim'] = ""
            entry['data'] = []

            jockeyentry = copy.deepcopy(entry)
            trainerentry = copy.deepcopy(entry)
            ownerentry = copy.deepcopy(entry)

            horsedatasets.append(entry)
            jockeydatasets.append(jockeyentry)
            trainerdatasets.append(trainerentry)
            ownerdatasets.append(ownerentry)
            existing.append(card.horse_name)

    # Add data by year to each horse dataset
    for horse in equibasehorses:
        for entry in horsedatasets:
            if str(horse.horsename) == str(entry['label']):
                stats = {}
                stats['year'] = horse.raceyear
                stats['vals'] = {}
                stats['vals']['winpercentage'] = int(
                        100*float(horse.winpercentage))
                stats['vals']['referencenumber'] = horse.referencenumber
                stats['vals']['earnings'] = money(float(horse.earnings))
                stats['vals']['earningsfloat'] = float(horse.earnings)
                stats['vals']['equibaserank'] = horse.equibaserank
                stats['vals']['equibasestarts'] = int(horse.equibasestarts)
                stats['vals']['place'] = int(horse.place)
                stats['vals']['speedfigure'] = int(horse.speedfigure)
                stats['vals']['topthreepercent'] = int(
                    100*float(horse.topthreepercent))
                stats['vals']['equibaseshow'] = int(horse.equibaseshow)
                stats['vals']['win'] = int(horse.win)
                stats['vals']['topthree'] = int(horse.topthree)
                entry['data'].append(stats)

    # Add data by year to each jockey dataset
    for jockey in equibasejockeys:
        for jockeyentry in jockeydatasets:
            if (str(jockey.equibaseidentity) == str(jockeyentry['jockeyid']) and str(jockeyentry['jockeyname']) != "None"):
                jockeystats = {}
                jockeystats['year'] = jockey.raceyear
                jockeystats['vals'] = {}
                jockeystats['vals']['winpercentage'] = int(
                        100*float(jockey.winpercentage))
                jockeystats['vals']['earnings'] = money(float(jockey.earnings))
                jockeystats['vals']['earningsfloat'] = float(jockey.earnings)
                jockeystats['vals']['equibaserank'] = jockey.equibaserank
                jockeystats['vals']['place'] = int(jockey.place)
                jockeystats['vals']['equibasestarts'] = int(jockey.equibasestarts)
                jockeystats['vals']['perstart'] = money(float(jockey.perstart))
                jockeystats['vals']['perstartfloat'] = float(jockey.perstart)
                jockeystats['vals']['topthreepercent'] = int(
                    100*float(jockey.topthreepercent))
                jockeystats['vals']['equibaseshow'] = int(jockey.equibaseshow)
                jockeystats['vals']['win'] = int(jockey.win)
                jockeystats['vals']['topthree'] = int(jockey.topthree)
                jockeyentry['data'].append(jockeystats)

    # Add data by year to each trainer dataset
    for trainer in equibasetrainers:
        for trainerentry in trainerdatasets:
            if (str(trainer.equibaseidentity) == str(trainerentry['trainerid']) and str(trainerentry['trainername']) != "None"):
                trainerstats = {}
                trainerstats['year'] = trainer.raceyear
                trainerstats['vals'] = {}
                trainerstats['vals']['wpsperstarter'] = float(trainer.wpsperstarter)
                trainerstats['vals']['earningsperstarter'] = money(float(trainer.earningsperstarter))
                trainerstats['vals']['earningsperstarterfloat'] = float(trainer.earningsperstarter)
                trainerstats['vals']['winpercentage'] = int(
                        100*float(trainer.winpercentage))
                trainerstats['vals']['starters'] = int(trainer.starters)
                trainerstats['vals']['earnings'] = money(float(trainer.earnings))
                trainerstats['vals']['earningsfloat'] = float(trainer.earnings)
                trainerstats['vals']['equibaserank'] = trainer.equibaserank
                trainerstats['vals']['place'] = int(trainer.place)
                trainerstats['vals']['equibasestarts'] = int(trainer.equibasestarts)
                trainerstats['vals']['perstart'] = money(float(trainer.perstart))
                trainerstats['vals']['perstartfloat'] = float(trainer.perstart)
                trainerstats['vals']['topthreepercent'] = int(
                    100*float(trainer.topthreepercent))
                trainerstats['vals']['equibaseshow'] = int(trainer.equibaseshow)
                trainerstats['vals']['win'] = int(trainer.win)
                trainerstats['vals']['startsperstarter'] = float(trainer.startsperstarter)
                trainerstats['vals']['topthree'] = int(trainer.topthree)
                trainerentry['data'].append(trainerstats)

    # Add data by year to each owner dataset
    for owner in equibaseowners:
        for ownerentry in ownerdatasets:
            if (str(owner.equibaseidentity) == str(ownerentry['ownerid']) and str(ownerentry['ownername']) != "None"):
                ownerstats = {}
                ownerstats['year'] = owner.raceyear
                ownerstats['vals'] = {}
                ownerstats['vals']['winpercentage'] = int(
                        100*float(owner.winpercentage))
                ownerstats['vals']['earnings'] = money(float(owner.earnings))
                ownerstats['vals']['earningsfloat'] = float(owner.earnings)
                ownerstats['vals']['equibaserank'] = owner.equibaserank
                ownerstats['vals']['place'] = int(owner.place)
                ownerstats['vals']['equibasestarts'] = int(owner.equibasestarts)
                ownerstats['vals']['perstart'] = money(float(owner.perstart))
                ownerstats['vals']['perstartfloat'] = float(owner.perstart)
                ownerstats['vals']['topthreepercent'] = int(
                    100*float(owner.topthreepercent))
                ownerstats['vals']['equibaseshow'] = int(owner.equibaseshow)
                ownerstats['vals']['win'] = int(owner.win)
                ownerstats['vals']['topthree'] = int(owner.topthree)
                ownerentry['data'].append(ownerstats)

    # Get Today's Horse Info
    horseEntries = []
    for card in cards:
        if card.horse_name in equibasehorsenames:
            horseinfo = {}
            horseinfo['horse_name'] = card.horse_name
            horseinfo['my_integer_field'] = card.my_integer_field
            horseinfo['ml_odds'] = card.ml_odds
            try:
                odds = str(card.ml_odds).split("/")
                floatodds = int(odds[0])/int(odds[1])
                horseinfo['mloddsfloat'] = floatodds
            except:
                horseinfo['mloddsfloat'] = 0.0
            horseinfo['scratch_indicator'] = card.scratch_indicator
            horseinfo['referencenumber'] = [x.referencenumber for x in equibasehorses if x.horsename == card.horse_name][0]

        else:
            horseinfo = {}
            horseinfo['horse_name'] = card.horse_name
            horseinfo['my_integer_field'] = card.my_integer_field
            horseinfo['ml_odds'] = card.ml_odds
            try:
                odds = str(card.ml_odds).split("/")
                floatodds = int(odds[0])/int(odds[1])
                horseinfo['mloddsfloat'] = floatodds
            except:
                horseinfo['mloddsfloat'] = 0.0
            horseinfo['scratch_indicator'] = card.scratch_indicator
            horseinfo['referencenumber'] = "-"

        if card.horse_name in runnerinfohorses or card.horse_name in runnerinfohorses2:
            horseinfo['jockeyname'] = [str(x.jockeyname) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['jockeyid'] = [str(x.jockeyid) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['trainername'] = [str(x.trainername) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['trainerid'] = [str(x.trainerid) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['ownername'] = [str(x.ownername) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            if len(str(horseinfo['ownername'])) > 30:
                    horseinfo['ownername'] = str(horseinfo['ownername'])[0:29]+"..."
            horseinfo['ownerid'] = [str(x.ownerid) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['sirename'] = [str(x.sirename) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['damname'] = [str(x.damname) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['damsirename'] = [str(x.damsirename) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['breeder'] = [str(x.breeder) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            if len(str(horseinfo['breeder'])) > 30:
                    horseinfo['breeder'] = str(horseinfo['breeder'])[0:29]+"..."
            horseinfo['pp'] = [str(x.pp) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['age'] = [str(x.age) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['sex'] = [str(x.sex) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['med'] = [str(x.med).replace("1","") for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            horseinfo['jockeyweight'] = [str(x.jockeyweight) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            # horseinfo['mlodds'] = [x.mlodds for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
            # try:
            #     odds = str(x.mlodds).split("/")
            #     floatodds = int(odds[0])/int(odds[1])
            #     horseinfo['mloddsfloat'] = floatodds
            # except:
            #     horseinfo['mloddsfloat'] = 0.0
            horseinfo['claim'] = [money(float(x.claim)) for x in runnerinfo if str(x.horsename).split(" (")[0] == card.horse_name or x.horsename == card.horse_name][0]
        else:
            horseinfo['jockeyname'] = ""
            horseinfo['jockeyid'] = ""
            horseinfo['trainername'] = ""
            horseinfo['trainerid'] = ""
            horseinfo['ownername'] = ""
            horseinfo['ownerid'] = ""
            horseinfo['sirename'] = ""
            horseinfo['damname'] = ""
            horseinfo['damsirename'] = ""
            horseinfo['breeder'] = ""
            horseinfo['pp'] = ""
            horseinfo['age'] = ""
            horseinfo['sex'] = ""
            horseinfo['med'] = ""
            horseinfo['jockeyweight'] = ""
            # horseinfo['mlodds'] = ""
            horseinfo['claim'] = ""
        horseEntries.append(horseinfo)

    # Get Horse Start and End Years
    try:
        horseequibaseraceyears = list(set([int(x.raceyear) for x in equibasehorses]))
        horseequibaseraceyears.sort()
        horsemaxraceyear = horseequibaseraceyears[-1]
        horseminraceyear = horseequibaseraceyears[0]
    except:
        horseequibaseraceyears = [int(datetoday.year)]
        horsemaxraceyear = int(datetoday.year)
        horseminraceyear = int(datetoday.year)

    # Get Jockey Start and End Years
    try:
        jockeyequibaseraceyears = list(set([int(x.raceyear) for x in equibasejockeys]))
        jockeyequibaseraceyears.sort()
        jockeymaxraceyear = jockeyequibaseraceyears[-1]
        jockeyminraceyear = jockeyequibaseraceyears[0]
    except:
        jockeyequibaseraceyears = [int(datetoday.year)]
        jockeymaxraceyear = int(datetoday.year)
        jockeyminraceyear = int(datetoday.year)

    # Get Trainer Start and End Years
    try:
        trainerequibaseraceyears = list(set([int(x.raceyear) for x in equibasetrainers]))
        trainerequibaseraceyears.sort()
        trainermaxraceyear = trainerequibaseraceyears[-1]
        trainerminraceyear = trainerequibaseraceyears[0]
    except:
        trainerequibaseraceyears = [int(datetoday.year)]
        trainermaxraceyear = int(datetoday.year)
        trainerminraceyear = int(datetoday.year)

    # Get Owner Start and End Years
    try:
        ownerequibaseraceyears = list(set([int(x.raceyear) for x in equibaseowners]))
        ownerequibaseraceyears.sort()
        ownermaxraceyear = ownerequibaseraceyears[-1]
        ownerminraceyear = ownerequibaseraceyears[0]
    except:
        ownerequibaseraceyears = [int(datetoday.year)]
        ownermaxraceyear = int(datetoday.year)
        ownerminraceyear = int(datetoday.year)

    context = {
        'cards': cards,
        'race': race,
        'today': datetoday,
        'horseEntries': horseEntries,
        'urlday': urlday,
        'urlmonth': urlmonth,
        'urlyear': urlyear,
        'horsemaxraceyear': horsemaxraceyear,
        'horseminraceyear': horseminraceyear,
        'horseequibaseraceyears': horseequibaseraceyears,
        'jockeymaxraceyear': jockeymaxraceyear,
        'jockeyminraceyear': jockeyminraceyear,
        'jockeyequibaseraceyears': jockeyequibaseraceyears,
        'trainermaxraceyear': trainermaxraceyear,
        'trainerminraceyear': trainerminraceyear,
        'trainerequibaseraceyears': trainerequibaseraceyears,
        'ownermaxraceyear': ownermaxraceyear,
        'ownerminraceyear': ownerminraceyear,
        'ownerequibaseraceyears': ownerequibaseraceyears,
        'horsedatasets': horsedatasets,
        'jockeydatasets': jockeydatasets,
        'trainerdatasets': trainerdatasets,
        'ownerdatasets': ownerdatasets
    }

    return render(request, 'races/view_race.html', context)
