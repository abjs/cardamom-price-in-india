data = [
    {
        "seller": "Header Systems (India) Limited, Nedumkandam",
        "lots": "279",
        "arrived": "76648.5",
        "sold": "76648.5",
        "max": "1961.00",
        "avg": "1657.65",
        "time": "morning",
        "day": "05",
        "month": "12",
        "year": "2020",
        "date": "05-12-2020"
    }, {
        "seller": "Mas Enterprises, Vandanmettu",
        "lots": "280",
        "arrived": "72552",
        "sold": "72147.8",
        "max": "2401.00",
        "avg": "1666.06",
        "time": "evening",
        "day": "05",
        "month": "12",
        "year": "2020",
        "date": "05-12-2020"
    },
    {
        "seller": "CARDAMOM GROWERSFOREVER PRIVATE LIMITED",
        "lots": "244",
        "arrived": "50114.400",
        "sold": "49231.500",
        "max": "1991.00",
        "avg": "1652.66",
        "time": "morning",
        "day": "07",
        "month": "12",
        "year": "2020",
        "date": "07-12-2020"

    },
    {
        "seller": "The Kerala Cardamom Processing and Marketing Company Limited, Thekkady",
        "lots": "242",
        "arrived": "75491.8",
        "sold": "74219.7",
        "max": "2014.00",
        "avg": "1658.44",
        "time": "evening",
        "day": "07",
        "month": "12",
        "year": "2020",
        "date": "07-12-2020"
    }, {
        "seller": "SUGANDHAGIRI SPICES PROMOTERS&TRADERS Pvt Ltd",
        "lots": "204",
        "arrived": "50351.7",
        "sold": "44413.6",
        "max": "2054.00",
        "avg": "1664.82",
        "time": "morning",
        "day": "09",
        "month": "12",
        "year": "2020",
        "date": "09-12-2020"

    }, {
        "seller": "Spice More Trading Company, Kumily",
        "lots": "248",
        "arrived": "62885.7",
        "sold": "61780.9",
        "max": "1952.00",
        "avg": "1632.85",
        "time": "evening",
        "day": "09",
        "month": "12",
        "year": "2020",
        "date": "09-12-2020"
    }, {
        "seller": "Green Cardamom Trading Company",
        "lots": "265",
        "arrived": "71464.5",
        "sold": "71167.9",
        "max": "2029.00",
        "avg": "1729.11",
        "time": "morning",
        "day": "10",
        "month": "12",
        "year": "2020",
        "date":  "10-12-2020"
    }, {
        "seller": "South Indian Green Cardamom Company Ltd, Kochi",
        "lots": "310",
        "arrived": "84326.3",
        "sold": "83699.2",
        "max": "2056.00",
        "avg": "1713.89",
        "time": "evening",
        "day": "10",
        "month": "12",
        "year": "2020",
        "date": "10-12-2020"
    }, {
        "seller": "Green House Cardamom Mktg.India Pvt. Ltd",
        "lots": "208",
        "arrived": "31208.8",
        "sold": "30564.8",
        "max": "2089.00",
        "avg": "1674.56",
        "time": "morning",
        "day": "11",
        "month": "12",
        "year": "2020",
        "date": "11-12-2020"
    }, {
        "seller": "THE CARDAMOM PLANTERS MARKETING CO-OPERATIVE SOCIETY LIMITED",
        "lots": "237",
        "arrived": "70303.3",
        "sold": "70108.3",
        "max": "2101.00",
        "avg": "1721.77",
        "time": "evening",
        "day": "11",
        "month": "12",
        "year": "2020",
        "date": "11-12-2020"
    }, {

        "seller": "Cardamom Planters Association, Santhanpara",
        "lots": "221",
        "arrived": "45572.2",
        "sold": "45209.7",
        "max": "1915.00",
        "avg": "1698.98",
        "time": "morning",
        "day": "12",
        "month": "12",
        "year": "2020",
        "date": "12-12-2020"
    }, {
        "seller": "Header Systems (India) Limited, Nedumkandam",
        "lots": "268",
        "arrived": "73178.1",
        "sold": "72707.8",
        "max": "2146.00",
        "avg": "1728.88",
        "time": "evening",
        "day": "12",
        "month": "12",
        "year": "2020",
        "date": "12-12-2020"
    }, {
        "seller": "Mas Enterprises, Vandanmettu",
        "lots": "301",
        "arrived": "78771",
        "sold": "78379.",
        "max": "2458.00",
        "avg": "1788.65",
        "time": "morning",
        "day": "14",
        "month": "12",
        "year": "2020",
        "date": "14-12-2020"

    }, {
        "seller": "CARDAMOM GROWERSFOREVER PRIVATE LIMITED",
        "lots": "182",
        "arrived": "35792.8",
        "sold": "35792.8",
        "max": "2141.00",
        "avg": "1775.56",
        "time": "evening",
        "day": "14",
        "month": "12",
        "year": "2020",
        "date": "14-12-2020"
    }
]

import config as env
import pymongo
from s import cardamom_price_add_to_database as inm
client = pymongo.MongoClient(env.Mogo_URL)
for i in data:
    inm(i,client,'price_new','today',"Abin")

