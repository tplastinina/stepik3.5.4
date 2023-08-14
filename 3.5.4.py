# 3.5.4

import requests
import json

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": 'efb8b87150c8f3c0c06a',
                      "client_secret": '598d7b96dc4a640c07030a1e17f4caa8'
                  })

# разбираем ответ сервера
j = json.loads(r.content.decode('utf-8'))

# достаем токен
token = j["token"]

artist = []

with open('C:/Users/tanze/Documents/Python/datten/dataset_24476_4.txt') as f:
    for artist_id in f:
        artist_id = artist_id.strip()
        params = {'xapp_token': token}
        res = requests.get(f'http://api.artsy.net/api/artists/{artist_id}', params=params).text
        data = json.loads(res)
        artist.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artist, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])




