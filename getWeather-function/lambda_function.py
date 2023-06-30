import json
import requests


def process_json_file(file_path):
    # Retrieving current weather data for all provinces in Spain
    with open(file_path, 'r') as f:
        data = json.load(f)

    results = []

    for inner_list in data:
        dictionary_object = inner_list[0]
        lat = dictionary_object['lat']
        long = dictionary_object['lon']
        response = make_api_call(lat, long)
        results.append(response)
    
    return results


    # count = len(results)
    # print(count)

def make_api_call(lat, lon):
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=08a8d302936096af9fd01832d92651df&units=metric"
    response = requests.get(API_URL)
    return response.json()
    

def lambda_handler(event, context):
    json_file_path = 'coordinates.json'
    currentWeather = process_json_file(json_file_path)
    
    
    print(currentWeather)
    
    # Take the timestamp of data retrieval
    for x in currentWeather:
        dt = x['dt']
        break

    file_name = f'{dt}.json'

    # TO DO
    
    return {
        'statusCode': 200,
        'body': 'Successfull function execution'
    }