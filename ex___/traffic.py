import requests,json
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

service_key = os.environ.get('SERVICE_KEY')

url = os.environ.get('API_URL') 


params = {
    "page" : 1,
    "perPage" : 10,
    "serviceKey" : service_key,
}
def call_response() :
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            # check_record(data)
            
            return data
        except Exception as e:
            print("JSON 파싱 실패:", e)
    else:
        print("Err:", response.status_code)


def print_data() :
    data = call_response()
    records = data['data']
    save_to_csv(records)
    for record in records:
        print(f'00시 00분 : {record['00시00분']} 상하구분 : {record['상하구분']} 역번호 {record['역번호']} ')



def check_record(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

def save_to_csv(data):
    df = pd.DataFrame(data)

    df.to_csv('result.csv',index=False,encoding='UTF-8')