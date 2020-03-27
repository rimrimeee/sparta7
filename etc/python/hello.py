import requests

bike = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99')
bike_json = bike.json()

for row in bike_json['rentBikeStatus']['row']:
    # 망원역 1번출구 앞 (9/22)

    rack_location = row['stationName'][5:]
    # rack_location = row['stationName'].split('. ')[1]
    rack_count = row['rackTotCnt']
    bike_count = row['parkingBikeTotCnt']

    print(rack_location + ' (' + bike_count + '/' + rack_count + ')')
    # print('{} ( {} / {} )'.format(rack_location,bike_count,rack_count))
