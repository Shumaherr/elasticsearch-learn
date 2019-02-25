import json
import random
from random import randrange
from datetime import datetime, timedelta
import requests
from dateutil.relativedelta import relativedelta


def check_date(timestamp_string):
    date_obj = datetime.strptime(timestamp_string, "%Y.%m.%d %H:%M:%S.%f")
    today = datetime.now()
    delta = today - relativedelta(months=1)
   
    if delta <= date_obj <= today:
        return True

es_url = "http://127.0.0.1:9200"

content = {
    "query": {
        "regexp":{
            "dst_ip": {
                "value": "192.0.2.(0|1)"
            }
        }
    }
}

headers = {"Content-Type": "application/json"}

json_obj = json.dumps(content)

payload = dict(filter_path = "took, hits.hits._source.timestamp, hits.hits._source.src_ip, hits.hits._source.url, hits.hits._source.user")
 
resp = requests.get(requests.compat.urljoin(es_url, "/_all/_search"), params=payload, data = json_obj, headers=headers)

print(resp.content)
json_resp = json.loads(resp.text)
response_dict = json.loads(resp.text)
print(response_dict.get("took"))
filtered_dict = {}
for x in range(response_dict["took"]):
    response_timestamp = response_dict["hits"]["hits"][x]["_source"]["timestamp"]
    if check_date(response_timestamp):
        filtered_dict = {**filtered_dict, **response_dict.get("hits").get("hits")[x].get("_source")}
 
        resp = requests.get(es_url + "/agentslog/locals/_search?q=src_ip:" + response_dict.get("hits").get("hits")[x].get("_source").get("src_ip"))
        if resp.status_code == 200:            
            response_dict = json.loads(resp.text)
            print(response_dict)
            for y in range(response_dict.get("hits").get("total")):
                print(response_dict.get("hits").get("hits")[y].get("_source").get('cmd'))
                filtered_dict['cmd'] = response_dict.get("hits").get("hits")[y].get("_source").get('cmd')
print(filtered_dict)
