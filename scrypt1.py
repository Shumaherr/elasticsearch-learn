import json
import random
from random import randrange
from datetime import datetime, timedelta
import requests

min_year = 2018
max_year = datetime.now().year
es_url = "http://127.0.0.1:9200"

start = datetime(min_year, 1, 1, 00, 00, 00)
years = max_year - min_year + 1
end = start + timedelta(days=365 * years)


def random_datetime(min_year=2018, max_year=datetime.now().year):
    start = datetime(min_year, 10, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = datetime.now()
    date = start + (end - start) * random.random()
    return date.strftime("%Y.%m.%d %H:%M:%S.%f")


def random_client_ip():
    return '192.168.' + str(random.randint(1, 255)) + '.' + str(random.randint(1, 255))


def random_server_ip():
    return '192.0.2.' + str(random.randint(0, 5))

url = 'https://127.0.0.1:9003'
user_list = ['Ivanov Ivan', 'Petrov Petr', 'Sidorov Sidor', 'Fedorov Fedor', 'Vladimirov Vladimir',
             'Valentinova Valentina', 'Anastasieva Anastasia', 'Irinova Irina0']
url_list = ['http://example1.com', 'http://example2.com', 'http://example3.com', 'http://example4.com',
            'http://example5.com', 'http://example6.com']
user_commands = ['curl', 'wget', 'hack', "traceroute"]

headers = {"Content-Type": "application/json"}

for x in range(20):
    request_dict = {
        'timestamp': random_datetime(),
        'user': random.choice(user_list), 
        'src_ip': random_client_ip(), 
        'dst_ip': random_server_ip(), 
        'url': random.choice(url_list),
        'cmd': random.choice(user_commands)
    }
    req1_dic = request_dict.copy()
    del req1_dic["cmd"]
    json_obj = json.dumps(req1_dic)
    r = requests.post(es_url + "/log/server", data=json_obj, headers=headers)
    print(r.content)
    req2_dic = request_dict.copy()
    del req2_dic['user']
    del req2_dic['dst_ip']
    del req2_dic['url']
    json_obj2 = json.dumps(req2_dic)
    
    f = requests.post(es_url + "/agentslog/locals", data=json_obj2, headers=headers)
    print(f.content)
