import requests
from colorama import Fore
import json

# out source url
url = 'http://168.119.202.31:8000/api/v2/crypto/'

# get currency info from url in json
json_info = requests.get(url).text

# convert info to dictionary
dict_info = json.loads(json_info)

# handel information in a for loop
for data in dict_info['data']:
	# print all information which get from url in consol

	print(Fore.BLUE + 'Name : ' + Fore.WHITE + data['name']) # print name of currency
	print(Fore.BLUE + 'Dollar Price : ' + Fore.WHITE + data['dollar_price']) # print dollar price of currency
	print(Fore.BLUE + 'Rial Price : ' + Fore.WHITE + data['rial_price']) # print rial price of currency
	print(Fore.BLUE + 'Daily Change : ' + Fore.WHITE + data['daily_change']) # print daily change of currency
	print(Fore.BLUE + 'Weekly Change : ' + Fore.WHITE + data['weekly_change']) # print weakly change of currency
	print(Fore.BLUE + 'Market Cap : ' + Fore.WHITE + data['market_cap']) # print market cap of currency
	print(Fore.RED + '**************************************')
