import requests


def write_to_file(city, units='metric', language='en',
                  api_key='your_api_key'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}&lang={language}'
    response = requests.get(url)
    content = response.json()

    with open('weather_data.txt', 'a') as file:
        for i in range(len(content['list'])):
            city_name = content['city']['name']
            date_and_time = content['list'][i]['dt_txt']
            temperature = content['list'][i].get('main').get('temp')
            condition = content['list'][i].get('weather')[0].get('main')

            file.write(f'{city_name},{date_and_time},{temperature},{condition}\n')


write_to_file('Antalya')