import requests, time, json

servers = ['maria.ru','rose.ru','sina.ru']

def send_request(url):
    request = requests.get(url)
    return request.content
    
#Не буду использовать шедуллер, сделаю самым простым способом. Пятница после рабочей недели всё-таки.
while True:
    for server in servers:
        response = json.load(send_request(server))
        print(f"{datetime.datetime.now().isoformat(timespec='seconds')}  {response['count']}")
    time.sleep(60)
    
