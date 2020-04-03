import requests
from pymongo import MongoClient



def scrap_and_insert():
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.bicycle
    bike = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
    bike_json = bike.json()

    for row in bike_json['rentBikeStatus']['row']:
        # 망원역 1번출구 앞 (9/22)

        rack_location = row['stationName'][5:]
        # rack_location = row['stationName'].split('. ')[1]
        rack_count = row['rackTotCnt']
        bike_count = row['parkingBikeTotCnt']

        print(rack_location + ' (' + bike_count + '/' + rack_count + ')')
        data = ({'rack_location': rack_location, 'rack_count': rack_count, 'bike_count': bike_count})
        db.insert_one(data)
        # print('{} ( {} / {} )'.format(rack_location,bike_count,rack_count))

def read_and_print():
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.bicycle
    all = list(db.find())
    for one in all:
        rack_location = one['rack_location']
        rack_count = one['rack_count']
        bike_count = one['bike_count']
        print('{} ( {}/{} )'.format(rack_location,bike_count,rack_count))

read_and_print()
