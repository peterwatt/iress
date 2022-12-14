import json

import requests

def lambda_handler(event, context):
    
    # Get city name from event
    city = event["queryStringParameters"]["city"]
    print('City is ' + city)
    
    # Call OpenWeatherMap API
    api_key = 'key-deleted'
    api_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    response = requests.get(api_url, params=params)
    
    
    return {
        "statusCode": 200,
        "body": json.dumps(response.json())
    }
