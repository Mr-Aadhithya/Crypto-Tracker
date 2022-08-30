import json
from wsgiref import headers
import requests

headers ={
    'X-CMC_PRO_API_KEY' : 'd6f394d4-3dc2-4d3d-9293-25f39c5693be', #apikey from coinmarketcap
    'Accepts' : 'application/json'

}

params={
    'start' :  '1',
    'limit' :  '5',
    'convert' : 'INR'

}
url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json=requests.get(url,params=params,headers=headers).json()

#print(json)

coins =json['data']

print("All prices in ruprees")

for x in coins:
    
    print(x['symbol'],x['quote']['INR']['price'])

