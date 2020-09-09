import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_user_info(user_api):
    try:
        respone = requests.get(user_api, stream=True)
        print(respone.content)
        return respone.status_code
    except requests.exceptions.RequestException as e:
       return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=50) as executor:

        user_api_list = [
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=1',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=2',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=3',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=4',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=3',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=4',
            '....',
            'http://sampleapi.com/v1/users/?apiKey=API_KEY&user_id=10000',
        ]

        for user_api in user_api_list:
            threads.append(executor.submit(get_user_info(user_api)))
           
    for task in as_completed(threads):
        print(task.result())
      
runner()
