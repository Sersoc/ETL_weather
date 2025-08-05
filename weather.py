import requests,datetime
from dotenv import load_dotenv
import os
load_dotenv()

service_key = os.environ.get('SERVICE_KEY')

url = os.environ.get('API_URL') 


now = datetime.datetime.now()

    # %H%M%S
date_str = now.strftime('%Y%m%d')
time_str = now.strftime('%H') + '00'
print(date_str)

# url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
# service_key = "WoNkkw1uJ00FRow19uGkuiCHnz4ITkoNLLUL2jYEHpSVK4So30LzrAQb36gHVAcw0pd8A23N040tvb7NIiELog=="

# params = {
#     "serviceKey" : service_key,
#     "numOfRows" : "100",
#     "pageNo" : "1",    
#     "dataType" : "JSON",
#     "base_date" : "20250725",
#     "base_time" : "0600",
#     "nx" : "55",
#     "ny" : "127"

# }

params = {
    "serviceKey": service_key,           # URL 인코딩 필요 시 처리
    "numOfRows": "100",
    "pageNo": "1",
    "dataType": "JSON",
    "base_date": date_str,             # 오늘 날짜
    "base_time": time_str,                 # 반드시 정시로 설정 (예: 0600, 1500 등)
    "nx": "55",
    "ny": "127"
}
def get_wether_data():
    response = requests.get(url,params=params)
    data = response.json()
    records = data['response']['body']['items']['item']

    return records
    # for record in records:
    #     print(f'{record['category']}{record['obsrValue']}')
    # print(response.content)